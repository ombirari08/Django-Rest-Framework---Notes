# from django.http import JsonResponse
# from students.models import Student
from django.shortcuts import render , get_object_or_404
from students.models import Student
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .serializers import StudentSerializer, EmployeeSerializer
from rest_framework.views import APIView
from employees.models import Employee
from django.http import Http404
from rest_framework import mixins, generics
from rest_framework import generics, mixins, viewsets
from rest_framework.generics import GenericAPIView 
from blogs.models import Blog , Comment
from blogs.serializers import BlogSerializer, CommentSerializer

# send data or 
@api_view(['GET', 'POST'])
def studentsView(request):
    if request.method =='GET':
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# Get this data one by one using primary key any other operations using primary key
@api_view(['GET', 'PUT','DELETE'])  # <- THIS FIXES THE ISSUE
def studentsDeatilView(request, pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method=='GET':
        serializer = StudentSerializer(student)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # updating the data 
    elif request.method=='PUT':
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else: 
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method=='DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# class based view code   
# class Employees(APIView):
# # get this data from Employees table
#     def get(self,request):
#         employees = Employee.objects.all()
#         serializer = EmployeeSerializer(employees, many= True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

# # post data to in Employees table 
#     def post(self, request):
#         serializer = EmployeeSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


# # get this EmployeesDetail and perform operation using primary key = pk
# class EmployeesDetail(APIView):
#     def get_object(self, pk):
#         try:
#             return Employee.objects.get(pk=pk)
#         except Employee.DoesNotExist:
#             raise Http404
#     def get(self, request, pk):
#         employee = self.get_object(pk=pk)
#         serializer = EmployeeSerializer(employee)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
#     def put(self, request, pk):
#         employee = self.get_object(pk)
#         serializer = EmployeeSerializer(employee, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk):
#         employee = self.get_object(pk)
#         employee.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

"""
#mixins Example
class Employees(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get(self, request):
        return self.list(request)
    
    def post(self, request):
        return self.create(request)
    
class EmployeesDetail(mixins.RetrieveModelMixin,mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    # RetrieveModelMixin Model Exmaple 
    def get(self, request, pk):
         return self.retrieve(request, pk)
    # updateModelMixin Model Exmaple 
    def put(self,request, pk):
        return self.update(request, pk)
    # destroyModelMixin Model Exmaple 
    def delete(self,request, pk):
        return self.destroy(request, pk)

"""

"""
#generics View
class Employees(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeesDetail(generics.RetrieveAPIView, generics.UpdateAPIView, generics.DestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = 'pk'
"""

# List and Create Data Using Viewsets
# class EmployeeViewset(viewsets.ViewSet):
#     def list(self, request):
#         queryset = Employee.objects.all()
#         serializer = EmployeeSerializer(queryset, many=True)
#         return Response (serializer.data)
    
#     def create(self, request):
#         serializer = EmployeeSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors)
    
#     # fetch single record using primary key - and urls handels routers 
#     def retrieve(self, request, pk=None):
#         employee = get_object_or_404(Employee, pk=pk)
#         serializer = EmployeeSerializer(employee)
#         return Response(serializer.data, status=status.HTTP_200_OK)


# You can perform all operations(Create ,update, delete) using modelviewset (3 line of code) 
# With ModelViewSet, you can create a full API like this:
class EmployeeViewset(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


# Blog App Code start for nested Serializer

class BlogsViews(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class CommentsViews(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer



class BlogDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    lookup_field = 'pk'

class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_field = 'pk'




    


