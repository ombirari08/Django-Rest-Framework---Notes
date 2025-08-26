# Django REST Framework - Notes API 📝

A simple Notes API built using **Django REST Framework (DRF)**. This project serves as both a practical example and an educational reference for building RESTful APIs in Django.

---

## 📘 Introduction to Django REST Framework (DRF)

### ❓ What is Django REST Framework?

Django REST Framework (DRF) is a powerful and flexible toolkit for building Web APIs using Django.

- Built on top of Django
- Helps build RESTful APIs
- Easily serialize data, handle requests, and manage authentication

---

### ✅ Why Use DRF?

| Benefit          | Description                                                  |
|------------------|--------------------------------------------------------------|
| Ease of Use      | High-level abstractions make API development quick and easy |
| Serialization    | Convert Django models to JSON/XML and vice versa            |
| Authentication   | Support for JWT, OAuth2, Token Auth                         |
| Browsable API    | Interactive UI for testing endpoints                        |
| Flexibility      | Supports both function-based and class-based views          |
| Community Support| Popular, well-documented, and widely used                   |

---

### 🔍 DRF vs Regular Django

| Feature         | Django                  | Django REST Framework     |
|----------------|--------------------------|----------------------------|
| Target          | Web apps (HTML views)   | APIs (JSON/XML responses) |
| UI Output       | HTML Templates          | JSON/XML                  |
| Views           | Views, TemplateViews    | APIView, ViewSets         |
| Forms           | Django Forms            | DRF Serializers           |

---

## 🔗 API (Application Programming Interface)

### ✅ What is an API?

An API is a set of rules that allows software systems to communicate.

- Acts as a bridge between frontend and backend
- Sends requests and receives responses, usually in JSON or XML

### ✅ Why APIs Matter

- Connect web/mobile frontend with backend services
- Use external systems (e.g., payment, weather)
- Keep systems modular and scalable

---

## 🌐 REST API

### ✅ What is a REST API?

A **REST API** is an architectural style that uses HTTP methods for communication. It's widely used in modern web development.

### ✅ Key Features of REST

- Simple & scalable
- Stateless
- Works with standard HTTP methods
- Language-independent
- Supports CRUD operations clearly

---

## 🔁 Serialization & Deserialization in DRF

### 🛠️ What is Serialization?

Converts complex Django model/queryset data into JSON/XML for client-side use.

**Analogy**: Like a translator converting English (model) into French (JSON) for a friend (frontend).

DRF provides `ModelSerializer` to make this easier:
- Auto maps model fields
- Works like Django model forms

### 🔁 What is Deserialization?

Reverse process of taking client data (JSON) and converting it back into Django model instances.

**Flow**:
- Client → JSON → Deserialization → Django Model
- Django Model → Serialization → JSON → Client

---

## 🧱 APIView in DRF

### ✅ What is APIView?

`APIView` is a class-based view in DRF that helps structure HTTP methods (GET, POST, PUT, DELETE).

1. **Example**
   ```python
    from rest_framework.views import APIView
    from rest_framework.response import Response
    
    class HelloAPIView(APIView):
        def get(self, request):
            return Response({"message": "Hello, world!"})

2. **Create a Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate
3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
4. **Set Up MySQL Database**
   - Create a MySQL database (e.g., blood_donor_db)
   - Open settings.py and update your database configuration:  
   ```bash
       DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'blood_donor_db',
            'USER': 'your_username',
            'PASSWORD': 'your_password',
            'HOST': 'localhost',
            'PORT': '3306',
        }
    }
5. **Apply Migrations**
   ```bash
   python manage.py makemigrations
   python manage.py makemigrations
2. **Run the Server**
   ```bash
   python manage.py runserver
## Mixins in Django REST Framework
### 🔁  What Are Mixins?
Mixins are reusable code classes in object-oriented programming that provide specific functionalities to our application. In Django REST Framework (DRF), mixins are used to add common functionalities to views such as Create, Read, Update, and Delete (CRUD) operations.
### 🔁  Why Use Mixins?
In the previous lecture, you saw that we had to write many lines of code for a single CRUD operation—even
after extending the APIView class in our class-based views.
But here’s the good news: we can simplify our code further by extending mixin classes with our class-based views..
Define :Mixins in Django REST Framework (DRF) are reusable classes that provide pre-built methods for common actions like listing, creating, retrieving, updating, and deleting objects.
## Built-in Mixins in Django REST Framework

Django REST Framework provides five built-in mixins to handle common CRUD functionalities, allowing you to avoid repetitive code throughout your application.

### 1. ListModelMixin
- **Purpose:** Returns a list of objects.
- **Method:** `list()`

### 2. CreateModelMixin
- **Purpose:** Creates a new object in the database.
- **Method:** `create()`

### 3. RetrieveModelMixin
- **Purpose:** Retrieves a single object (e.g., one employee record).
- **Method:** `retrieve()`

### 4. UpdateModelMixin
- **Purpose:** Updates an existing object using its primary key.
- **Method:** `update()`

### 5. DestroyModelMixin
- **Purpose:** Deletes an object using its primary key.
- **Method:** `destroy()`

Each mixin provides a specific built-in method that simplifies the implementation of standard CRUD operations in your API views.
1. **Example of Using Mixins**
   ```python
    from rest_framework import generics, mixins
    from .models import Employee
    from .serializers import EmployeeSerializer
    
    class EmployeeView(mixins.ListModelMixin,
                       mixins.CreateModelMixin,
                       generics.GenericAPIView):
        
        queryset = Employee.objects.all()
        serializer_class = EmployeeSerializer
    
        def get(self, request, *args, **kwargs):
            return self.list(request, *args, **kwargs)
    
        def post(self, request, *args, **kwargs):
            return self.create(request, *args, **kwargs)
   #You can add other mixins like RetrieveModelMixin, UpdateModelMixin, and DestroyModelMixin in similar ways, depending on the functionality you need

### What Are Generic Views?

Generic views in Django REST Framework are **pre-built class-based views** that provide commonly used patterns for handling API requests. They combine the functionality of views, mixins, and serializers to reduce boilerplate code and streamline API development.

They are built on top of Django’s class-based views and DRF’s mixins, offering ready-to-use implementations for common operations like:

- Listing objects
- Creating objects
- Retrieving objects
- Updating objects
- Deleting objects

---

### Why Use Generic Views?

- Simplify your code by reusing common patterns.
- Reduce duplication in your views.
- Combine mixins and logic automatically.
- Great for standard CRUD operations.

---

### Commonly Used Generic Views

| Generic View Class           | Description                                     |
|------------------------------|-------------------------------------------------|
| `ListAPIView`               | Returns a list of objects (GET only)            |
| `CreateAPIView`             | Creates a new object (POST only)                |
| `RetrieveAPIView`           | Retrieves a single object by ID (GET)           |
| `UpdateAPIView`             | Updates an existing object (PUT/PATCH)          |
| `DestroyAPIView`            | Deletes an object (DELETE)                      |
| `ListCreateAPIView`         | Combines listing and creation (GET & POST)      |
| `RetrieveUpdateAPIView`     | Combines retrieve and update (GET, PUT, PATCH)  |
| `RetrieveDestroyAPIView`    | Retrieve and delete (GET, DELETE)               |
| `RetrieveUpdateDestroyAPIView` | All three: retrieve, update, delete         |

---

1. **Example: Using `ListCreateAPIView**
   ```python
    from rest_framework.generics import ListCreateAPIView
    from .models import Employee
    from .serializers import EmployeeSerializer
    
    class EmployeeListCreateView(ListCreateAPIView):
        queryset = Employee.objects.all()
        serializer_class = EmployeeSerializer

## ViewSets in Django REST Framework
### What Are ViewSets?

ViewSets are a higher-level abstraction in Django REST Framework that combine the logic for a set of related views into a single class. Instead of defining separate views for each HTTP method or action (like list, create, retrieve, update, delete), a ViewSet groups them together, making your code more concise and organized.

---

### Why Use ViewSets?

- **Simplifies code** by consolidating multiple views into one class.
- **Automatically provides standard actions** for CRUD operations.
- Works seamlessly with **routers** to generate URL patterns automatically.
- Reduces boilerplate and improves maintainability.

---

### Types of ViewSets

| ViewSet Type              | Description                                                     |
|--------------------------|-----------------------------------------------------------------|
| `ViewSet`                | Base class, requires explicit method definitions.               |
| `GenericViewSet`         | Extends `ViewSet` with generic view behavior and mixin support. |
| `ModelViewSet`           | Combines `GenericViewSet` with mixins for full CRUD operations. |

---

### Common Actions Provided by ViewSets

- `list()` — Return a list of all objects.
- `create()` — Create a new object.
- `retrieve()` — Retrieve a specific object by ID.
- `update()` — Update an existing object.
- `partial_update()` — Partially update an existing object.
- `destroy()` — Delete an object.

---

1. **Example: Using a ViewSets**
   ```python
    from rest_framework import viewsets
    from rest_framework.response import Response
    from rest_framework import status
    from .models import Employee
    from .serializers import EmployeeSerializer
    
    class EmployeeViewSet(viewsets.ViewSet):
    
        def list(self, request):
            employees = Employee.objects.all()
            serializer = EmployeeSerializer(employees, many=True)
            return Response(serializer.data)
    
        def retrieve(self, request, pk=None):
            try:
                employee = Employee.objects.get(pk=pk)
            except Employee.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = EmployeeSerializer(employee)
            return Response(serializer.data)
    
        def create(self, request):
            serializer = EmployeeSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  

2. **URL Routing with ViewSets**
   ```python
   from rest_framework.routers import DefaultRouter
   from .views import EmployeeViewSet
  
   router = DefaultRouter()
   router.register(r'employees', EmployeeViewSet)
  
   urlpatterns = router.urls

### Common Actions Provided by ViewSets

- GET /employees/ → list employees
- POST /employees/ → create employee
- GET /employees/{id}/ → retrieve employee
- PUT /employees/{id}/ → update employee
- PATCH /employees/{id}/ → partial update
- DELETE /employees/{id}/ → delete employee

---
### When to Use ViewSets

- When you want to quickly build a full set of CRUD API endpoints.
- When you want automatic URL routing.
- When your API fits the standard REST pattern.
- If you need highly customized behavior, you can override individual methods inside the ViewSet or use APIView for full control.

---
## ModelViewSet in Django REST Framework

### What is a ModelViewSet?

A **ModelViewSet** is a powerful class in Django REST Framework that combines the functionality of `GenericViewSet` with built-in mixins for all CRUD (Create, Read, Update, Delete) operations. It provides default implementations of the common actions, so you don't have to write these methods yourself.

---

### Key Features

- Supports all standard CRUD operations by default:
  - `list()` — List all objects
  - `create()` — Create a new object
  - `retrieve()` — Retrieve an object by its ID
  - `update()` — Update an existing object
  - `partial_update()` — Partially update an object
  - `destroy()` — Delete an object
- Requires minimal code: just specify the `queryset` and `serializer_class`.
- Supports overriding any method to customize behavior.
- Works seamlessly with routers to automatically generate URL patterns.

---

### What Are ModelViewSet?
A **ModelViewSet** is a powerful class in Django REST Framework that combines the functionality of `GenericViewSet` with built-in mixins for all CRUD (Create, Read, Update, Delete) operations. It provides default implementations of the common actions, so you don't have to write these methods yourself.

---


### Key Features

- Supports all standard CRUD operations by default:
  - `list()` — List all objects
  - `create()` — Create a new object
  - `retrieve()` — Retrieve an object by its ID
  - `update()` — Update an existing object
  - `partial_update()` — Partially update an object
  - `destroy()` — Delete an object
- Requires minimal code: just specify the `queryset` and `serializer_class`.
- Supports overriding any method to customize behavior.
- Works seamlessly with routers to automatically generate URL patterns.

---
1. **Example of a ModelViewSet**
   ```python
    from rest_framework import viewsets
    from .models import Employee
    from .serializers import EmployeeSerializer
    
    class EmployeeModelViewSet(viewsets.ModelViewSet):
        queryset = Employee.objects.all()
        serializer_class = EmployeeSerializer

## Nested Serializers in Django REST Framework

### What is a Nested Serializer?

A **nested serializer** is a serializer that includes another serializer as a field. It's used when your models have relationships (like `ForeignKey`, `OneToOneField`, or `ManyToManyField`) and you want to represent related data within the same API response.

This allows you to include detailed information from related models directly in your serialized output, instead of just showing an ID or foreign key.

---

### When to Use Nested Serializers

Use nested serializers when:
- You want to display related object data in the API.
- You want to handle object creation or updates that involve related models.
- You’re working with one-to-many or one-to-one relationships.

---

### Example Scenario

Let’s say we have two models: `Department` and `Employee`. Each employee belongs to a department.
1. **Example of a ModelViewSet**
   ```python
    # models.py
    from django.db import models
    
    class Department(models.Model):
        name = models.CharField(max_length=100)
    
    class Employee(models.Model):
        name = models.CharField(max_length=100)
        email = models.EmailField()
        department = models.ForeignKey(Department, on_delete=models.CASCADE)


3. **Step 1: Create Serializers**
   ```python
    # serializers.py
    from rest_framework import serializers
    from .models import Department, Employee
    
    class DepartmentSerializer(serializers.ModelSerializer):
        class Meta:
            model = Department
            fields = ['id', 'name']
    
    class EmployeeSerializer(serializers.ModelSerializer):
        department = DepartmentSerializer()
    
        class Meta:
            model = Employee
            fields = ['id', 'name', 'email', 'department']
5. **Now when you serialize an Employee, it will show the full department details instead of just the department ID:**
   ```python
      {
      "id": 1,
      "name": "John Doe",
      "email": "john@example.com",
      "department": {
        "id": 1,
        "name": "Engineering"
      }
    }

## Nested Serializers in Django REST Framework



