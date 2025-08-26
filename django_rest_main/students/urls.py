from django.urls import path
from . import views  # make sure views.py exists too

urlpatterns = [
    # Example route
    path('', views.students, name='home'),
]
