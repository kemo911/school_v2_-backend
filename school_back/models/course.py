import uuid

from django.db import models


class CourseCategory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=2550)

    class Meta:
        db_table = 'CourseCategory'


class CourseModule(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=2550)

    class Meta:
        db_table = 'CourseModule'


class CourseModuleItems(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=2550)

    class Meta:
        db_table = 'CourseModuleItems'


class Course(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=2550)
    code = models.CharField(max_length=10)
    createdAt = models.DateTimeField()
    status = models.BooleanField()
    category = models.ForeignKey(CourseCategory, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Course'
