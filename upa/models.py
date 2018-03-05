from django.db import models
from django_upload_path.upload_path import auto_cleaned_path_uuid4


class Soubor(models.Model):
    soubor = models.FileField(upload_to=auto_cleaned_path_uuid4)
