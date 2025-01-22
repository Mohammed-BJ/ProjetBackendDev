from django.http import HttpResponse
from rest_framework import viewsets
from .models import Candidate, Recruiter
from .serializers import CandidateSerializer, RecruiterSerializer

class CandidateViewSet(viewsets.ModelViewSet):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer

class RecruiterViewSet(viewsets.ModelViewSet):
    queryset = Recruiter.objects.all()
    serializer_class = RecruiterSerializer

def home(request):
    return HttpResponse("Welcome to the Recruitment API")