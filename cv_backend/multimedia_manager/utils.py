from django.core.exceptions import ValidationError

def validate_image_file(file):
    """Ensure that only allowed image file formats are accepted."""
    allowed_extensions = ['jpg', 'jpeg', 'png', 'gif']
    file_extension = file.name.split('.')[-1].lower()
    if file_extension not in allowed_extensions:
        raise ValidationError(f"Unsupported file extension '{file_extension}'. Allowed extensions: {', '.join(allowed_extensions)}")
