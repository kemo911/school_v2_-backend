from django.contrib import admin
from .models import Course, CourseCatalog, CustomUser, Student, Professor, Advisor

admin.site.register(Course)
admin.site.register(CourseCatalog)
admin.site.register(CustomUser)
admin.site.register(Student)
admin.site.register(Professor)
admin.site.register(Advisor)
