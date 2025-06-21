from django.urls import path
from .views import process_excel

urlpatterns = [
    path('upload-excel/', process_excel),
]
