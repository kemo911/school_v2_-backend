import uuid
from datetime import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    pass


class Advisor(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    department = models.CharField(max_length=2)
    office_location = models.CharField(max_length=255)
    office_hours = models.JSONField()

    class Meta:
        db_table = 'Advisor'


class Student(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    dob = models.DateField(default=datetime.now())
    address = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=255)
    emergency_contact_number = models.CharField(max_length=255)
    enrollment_date = models.DateField(default=datetime.now())
    advisor = models.ForeignKey(Advisor, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Student'


class Professor(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    department = models.CharField(max_length=2)
    office_hours = models.CharField(max_length=255)

    class Meta:
        db_table = 'Professor'
