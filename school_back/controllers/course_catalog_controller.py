from django.http import JsonResponse
from ..models import CourseCatalog
from ..serializers import CourseCatalogSerializer


def list_course(request):
    courses = CourseCatalog.objects.all()
    serializer = CourseCatalogSerializer(courses, many=True)
    return JsonResponse(serializer.data, safe=False)
