from django.urls import path
from .views import StudentListCreateView,AdultsStudentView

urlpatterns = [
path('api/students/',
StudentListCreateView.as__view(),
name='student-list'),
path('api/students/adults/',
AdultStudentView.as__view(),
name="adult-students),
]
