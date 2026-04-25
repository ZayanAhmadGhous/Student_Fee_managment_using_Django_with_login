from rest_framework import viewsets
from .models import StudentFee
from .serializers import StudentFeeSerializer
from django.http import HttpResponse

# def home(request):
#     return HttpResponse("Welcome to Student Fee API 🚀")

class StudentFeeViewSet(viewsets.ModelViewSet):
    queryset = StudentFee.objects.all()
    serializer_class = StudentFeeSerializer