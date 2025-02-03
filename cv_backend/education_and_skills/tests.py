from django.test import TestCase
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from .models import Education, Skill, Course
from base_user.models import UserProfile

User = get_user_model()

class EducationTest(TestCase):

    def setUp(self):
        """
        Crear un usuario y su perfil para las pruebas.
        """
        group = Group.objects.create(name="Admin")
        self.user = User.objects.create_user(
            username="testuser",
            password="testpassword"
        )
        self.user.groups.add(group)
        self.profile = UserProfile.objects.get(user=self.user)

    def test_create_education(self):
        """
        Probar la creación de una formación.
        """
        education = Education.objects.create(
            user_profile=self.profile,
            title="Ingeniería en Sistemas",
            subtitle="Ingeniería",
            institution="Universidad de El Salvador",
            start_year=2015,
            end_year=2020,
            description="Formación en el área de sistemas informáticos."
        )
        self.assertEqual(education.title, "Ingeniería en Sistemas")

    def test_update_education(self):
        """
        Probar la actualización de una formación.
        """
        education = Education.objects.create(
            user_profile=self.profile,
            title="Ingeniería en Sistemas",
            subtitle="Ingeniería",
            institution="Universidad de El Salvador",
            start_year=2015,
            end_year=2020,
            description="Formación en el área de sistemas informáticos."
        )
        education.title = "Ingeniería en Informática"
        education.save()

        self.assertEqual(education.title, "Ingeniería en Informática")

    def test_delete_education(self):
        """
        Probar la eliminación de una formación.
        """
        education = Education.objects.create(
            user_profile=self.profile,
            title="Ingeniería en Sistemas",
            subtitle="Ingeniería",
            institution="Universidad de El Salvador",
            start_year=2015,
            end_year=2020,
            description="Formación en el área de sistemas informáticos."
        )
        education_id = education.id
        education.delete()

        self.assertFalse(Education.objects.filter(id=education_id).exists())


class SkillTest(TestCase):

    def setUp(self):
        """
        Crear un usuario y su perfil para las pruebas.
        """
        group = Group.objects.create(name="Admin")
        self.user = User.objects.create_user(
            username="testuser",
            password="testpassword"
        )
        self.user.groups.add(group)
        self.profile = UserProfile.objects.get(user=self.user)

    def test_create_skill(self):
        """
        Probar la creación de una habilidad.
        """
        skill = Skill.objects.create(
            user_profile=self.profile,
            title = "Python",
            category = "backend",
            proficiency = 50
        )
        self.assertEqual(skill.title, "Python")

    def test_update_skill(self):
        """
        Probar la actualización de una habilidad.
        """
        skill = Skill.objects.create(
            user_profile=self.profile,
            title = "Python",
            category = "backend",
            proficiency = 50
        )
        skill.proficiency = 75
        skill.save()

        self.assertEqual(skill.proficiency, 75)

    def test_delete_skill(self):
        """
        Probar la eliminación de una habilidad.
        """
        skill = Skill.objects.create(
            user_profile=self.profile,
            title = "Python",
            category = "backend",
            proficiency = 50
        )

        skill_id = skill.id
        skill.delete()

        self.assertFalse(Skill.objects.filter(id=skill_id).exists())


class CourseTest(TestCase):

    def setUp(self):
        """
        Crear un usuario y su perfil para las pruebas.
        """
        group = Group.objects.create(name="Admin")
        self.user = User.objects.create_user(
            username="testuser",
            password="testpassword"
        )
        self.user.groups.add(group)
        self.profile = UserProfile.objects.get(user=self.user)

    def test_create_course(self):
        """
        Probar la creación de un curso.
        """
        course = Course.objects.create(
            user_profile=self.profile,
            title="Curso de Python",
            platform = "Udemy",
            completion_year=2019,
            description="Curso de Python para principiantes."
        )
        self.assertEqual(course.title, "Curso de Python")

    def test_update_course(self):
        """
        Probar la actualización de un curso.
        """
        course = Course.objects.create(
            user_profile=self.profile,
            title="Curso de Python",
            platform = "Udemy",
            completion_year=2019,
            description="Curso de Python para principiantes."
        )
        course.title = "Curso de Django"
        course.save()

        self.assertEqual(course.title, "Curso de Django")

    def test_delete_course(self):
        """
        Probar la eliminación de un curso.
        """
        course = Course.objects.create(
            user_profile=self.profile,
            title="Curso de Python",
            platform = "Udemy",
            completion_year=2019,
            description="Curso de Python para principiantes."
        )
        course_id = course.id
        course.delete()

        self.assertFalse(Course.objects.filter(id=course_id).exists())
