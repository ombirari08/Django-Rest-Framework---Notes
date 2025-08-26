from django.urls import path ,include
from . import views
from rest_framework .routers import DefaultRouter
# List and Create Data Using Viewsets it used routers for handling urls
router = DefaultRouter()
router.register('Employees', views.EmployeeViewset, basename='employee')

urlpatterns = [
    path('students/', views.studentsView),
    path('students/<int:pk>', views.studentsDeatilView),
    
    # path('Employees/', views.Employees.as_view()),
    # path('Employees/<int:pk>', views.EmployeesDetail.as_view()),

    path('', include(router.urls)),

    path('blogs/', views.BlogsViews.as_view()),
    path('comment/', views.CommentsViews.as_view()),

    path('blogs/<int:pk>', views.BlogDetailView.as_view()),
    path('comment/<int:pk>', views.CommentDetailView.as_view()),


]