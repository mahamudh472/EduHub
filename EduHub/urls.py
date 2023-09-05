"""
URL configuration for EduHub project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('student-list', views.student_list, name='student-list'),
    path('add-student', views.add_student, name='add-student'),
    path('teacher-list', views.teacher_list, name='teacher-list'),
    path('add-teacher', views.add_teacher, name='add-teacher'),
    path('add-course', views.add_course, name='add-course'),
    path('course-list', views.course_list, name='course-list'),
    path('course-details/<int:id>', views.course_details, name='course-details'),
    path('student/<int:id>', views.single_student, name="single-student"),
    path('error', views.custom_404, name='error')
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)