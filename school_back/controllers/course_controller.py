from django.http import JsonResponse
from ..models import Course
from ..serializers import CourseSerializer


def list_course(request):
    courses = Course.objects.all()
    serializer = CourseSerializer(courses, many=True)
    return JsonResponse(serializer.data, safe=False)
