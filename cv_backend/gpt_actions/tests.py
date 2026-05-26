from datetime import date
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from base_user.models import CustomUser, UserProfile
from experiencia_laboral.models import ExperienciaLaboral
from projects.models import Project
from education_and_skills.models import Education, Skill, Course

class GPTActionsTestCase(APITestCase):

    def setUp(self):
        # 1. Create a Primary Test User & Profile
        self.user1 = CustomUser.objects.create_user(
            username='yampi_admin',
            email='yampi@example.com',
            password='testpassword123',
            role='admin'
        )
        # Ensure profile1 exists and has set values
        self.profile1, _ = UserProfile.objects.get_or_create(user=self.user1)
        self.profile1.nombre = 'Yampi'
        self.profile1.apellido = 'Developer'
        self.profile1.correo_electronico = 'yampi@example.com'
        self.profile1.profesion = 'programador_web'
        self.profile1.ciudad = 'Madrid'
        self.profile1.disponibilidad = True
        self.profile1.save()
        self.token1, _ = Token.objects.get_or_create(user=self.user1)

        # 2. Create an Impersonator/Second Test User & Profile for Isolation Testing
        self.user2 = CustomUser.objects.create_user(
            username='other_user',
            email='other@example.com',
            password='otherpassword123',
            role='guest'
        )
        # Ensure profile2 exists and has set values
        self.profile2, _ = UserProfile.objects.get_or_create(user=self.user2)
        self.profile2.nombre = 'Other'
        self.profile2.apellido = 'User'
        self.profile2.correo_electronico = 'other@example.com'
        self.profile2.profesion = 'programador_mobile'
        self.profile2.ciudad = 'Barcelona'
        self.profile2.disponibilidad = False
        self.profile2.save()
        self.token2, _ = Token.objects.get_or_create(user=self.user2)

        # Set up default credentials for user1
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token1.key}')

    def test_authentication_required(self):
        """
        Verify that requests without any authorization header return 401.
        """
        self.client.credentials()  # Clear credentials
        url = reverse('gpt-profile')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_authentication_with_invalid_token(self):
        """
        Verify that requests with an invalid/malformed token return 401.
        """
        self.client.credentials(HTTP_AUTHORIZATION='Bearer invalid_token_12345')
        url = reverse('gpt-profile')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_authentication_with_valid_token(self):
        """
        Verify that requests with a valid token succeed.
        """
        url = reverse('gpt-profile')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['nombre'], 'Yampi')

    def test_profile_retrieve_and_update(self):
        """
        Verify profile retrieve and patch behavior.
        """
        url = reverse('gpt-profile')
        
        # 1. Retrieve profile
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['ciudad'], 'Madrid')
        
        # 2. Update profile (PATCH)
        update_data = {
            'ciudad': 'Valencia',
            'nombre': 'Yampi Updated',
            'profesion': 'programador_mobile'
        }
        response = self.client.patch(url, update_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.profile1.refresh_from_db()
        self.assertEqual(self.profile1.ciudad, 'Valencia')
        self.assertEqual(self.profile1.nombre, 'Yampi Updated')
        self.assertEqual(self.profile1.profesion, 'programador_mobile')

    def test_experience_crud_and_soft_delete(self):
        """
        Verify complete CRUD on ExperienciaLaboral.
        Ensures creation auto-associates with user1, detail isolation, and soft delete behavior.
        """
        # Create user1 experience
        url_list = reverse('gpt-experiences-list')
        experience_data = {
            'empresa': 'Acme Corp',
            'posicion': 'Backend Developer',
            'descripcion': '<p>Developing APIs</p>',
            'fecha_inicio': '2024-01-01',
            'ubicacion': 'Madrid',
            'publicado': True
        }
        response = self.client.post(url_list, experience_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        experience_id = response.data['id']
        
        # Verify it was linked to profile1
        exp_obj = ExperienciaLaboral.objects.get(id=experience_id)
        self.assertEqual(exp_obj.user_profile, self.profile1)

        # Create user2 experience to test isolation
        other_exp = ExperienciaLaboral.objects.create(
            user_profile=self.profile2,
            empresa='Other Corp',
            posicion='iOS Developer',
            fecha_inicio=date(2023, 5, 1),
            ubicacion='Barcelona',
            publicado=True
        )

        # List experiences (should only return user1's experience)
        response = self.client.get(url_list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['empresa'], 'Acme Corp')

        # Retrieve detail of own experience
        url_detail = reverse('gpt-experiences-detail', kwargs={'pk': experience_id})
        response = self.client.get(url_detail)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['empresa'], 'Acme Corp')

        # Retrieve detail of other user's experience (should return 404)
        url_other_detail = reverse('gpt-experiences-detail', kwargs={'pk': other_exp.id})
        response = self.client.get(url_other_detail)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        # Update own experience (PATCH)
        response = self.client.patch(url_detail, {'empresa': 'Acme Inc.'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        exp_obj.refresh_from_db()
        self.assertEqual(exp_obj.empresa, 'Acme Inc.')

        # Update other user's experience (PATCH should return 404)
        response = self.client.patch(url_other_detail, {'empresa': 'Hacked'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        other_exp.refresh_from_db()
        self.assertEqual(other_exp.empresa, 'Other Corp')

        # Delete own experience (should perform SOFT delete, i.e., set publicado=False and return 204)
        response = self.client.delete(url_detail)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        exp_obj.refresh_from_db()
        self.assertFalse(exp_obj.publicado)

        # Delete other user's experience (DELETE should return 404)
        response = self.client.delete(url_other_detail)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_projects_isolation_and_hard_delete(self):
        """
        Verify isolation and hard delete on Project.
        """
        own_project = Project.objects.create(
            user_profile=self.profile1,
            title='My Portfolio',
            start_date=date(2023, 1, 1),
            order=1
        )
        other_project = Project.objects.create(
            user_profile=self.profile2,
            title='Other Project',
            start_date=date(2023, 2, 1),
            order=2
        )

        url_list = reverse('gpt-projects-list')
        url_detail = reverse('gpt-projects-detail', kwargs={'pk': own_project.id})
        url_other = reverse('gpt-projects-detail', kwargs={'pk': other_project.id})

        # List
        response = self.client.get(url_list)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'My Portfolio')

        # Retrieve other project
        response = self.client.get(url_other)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        # Hard delete own project
        response = self.client.delete(url_detail)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Project.objects.filter(id=own_project.id).exists())

    def test_education_isolation_and_hard_delete(self):
        """
        Verify isolation and hard delete on Education.
        """
        own_edu = Education.objects.create(
            user_profile=self.profile1,
            title='Computer Science Degree',
            institution='UAM',
            start_year=2018,
            end_year=2022
        )
        other_edu = Education.objects.create(
            user_profile=self.profile2,
            title='Art History',
            institution='UCM',
            start_year=2015,
            end_year=2019
        )

        url_list = reverse('gpt-education-list')
        url_detail = reverse('gpt-education-detail', kwargs={'pk': own_edu.id})
        url_other = reverse('gpt-education-detail', kwargs={'pk': other_edu.id})

        # List
        response = self.client.get(url_list)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Computer Science Degree')

        # Retrieve other edu
        response = self.client.get(url_other)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        # Hard delete
        response = self.client.delete(url_detail)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Education.objects.filter(id=own_edu.id).exists())

    def test_skills_isolation_and_proficiency_validation(self):
        """
        Verify isolation, proficiency limit validation, and hard delete on Skill.
        """
        own_skill = Skill.objects.create(
            user_profile=self.profile1,
            title='Python',
            category='backend',
            proficiency=90
        )
        other_skill = Skill.objects.create(
            user_profile=self.profile2,
            title='React',
            category='frontend',
            proficiency=80
        )

        url_list = reverse('gpt-skills-list')
        url_detail = reverse('gpt-skills-detail', kwargs={'pk': own_skill.id})
        url_other = reverse('gpt-skills-detail', kwargs={'pk': other_skill.id})

        # List
        response = self.client.get(url_list)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Python')

        # Retrieve other
        response = self.client.get(url_other)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        # Create skill validation error (proficiency = 120)
        invalid_skill_data = {
            'title': 'Rust',
            'category': 'backend',
            'proficiency': 120
        }
        response = self.client.post(url_list, invalid_skill_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('proficiency', response.data)

        # Hard delete
        response = self.client.delete(url_detail)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Skill.objects.filter(id=own_skill.id).exists())

    def test_courses_isolation_and_hard_delete(self):
        """
        Verify isolation and hard delete on Course.
        """
        own_course = Course.objects.create(
            user_profile=self.profile1,
            title='Django Advanced',
            platform='Udemy',
            completion_year=2024
        )
        other_course = Course.objects.create(
            user_profile=self.profile2,
            title='Swift Fundamentals',
            platform='Platzi',
            completion_year=2023
        )

        url_list = reverse('gpt-courses-list')
        url_detail = reverse('gpt-courses-detail', kwargs={'pk': own_course.id})
        url_other = reverse('gpt-courses-detail', kwargs={'pk': other_course.id})

        # List
        response = self.client.get(url_list)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Django Advanced')

        # Retrieve other
        response = self.client.get(url_other)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        # Hard delete
        response = self.client.delete(url_detail)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Course.objects.filter(id=own_course.id).exists())

    def test_openapi_schema_endpoint(self):
        """
        Verify that the schema view serves the YAML file correctly without authentication.
        """
        self.client.credentials()  # Clear credentials to test anonymous access
        url = reverse('gpt-schema')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('text/yaml', response['Content-Type'])
        self.assertIn(b'Private CV Management API', response.content)
