from django.shortcuts import render, redirect
from main.models import Student, Course, Teacher
from django.contrib import messages 


def index(request):
    total_students = Student.objects.count()
    total_teachers = Teacher.objects.count()
    total_courses = Course.objects.count() 
    context = {
        "total_students": total_students,
        "total_teachers": total_teachers,
        "total_courses": total_courses
    }
    return render(request, 'index.html', context)

def student_list(request):
    students = Student.objects.all() 
    course_list = Course.objects.all()
    return render(request, 'students_list.html', {'students': students, 'course_list': course_list})

def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request, 'teacher_list.html', {"teachers": teachers})

def add_student(request):
    if request.method == "POST":
        student  = Student()
        student.student_id = request.POST["student-id"]
        student.student_name = request.POST["student-name"]
        student.date_of_birth = request.POST["date-of-birth"]
        student.gender = request.POST["gender"]
        student.religion = request.POST["religion"]
        student.contact_number = request.POST["contact-number"]
        student.father_name = request.POST["father-name"]
        student.mother_name = request.POST["mother-name"]
        student.home_number = request.POST["home-number"]
        student.address = request.POST["address"]
        student.course = Course.objects.get(course_name=request.POST["course"])
        student.save()
        messages.add_message(request, messages.SUCCESS, "Student add sucsessfully")
        return redirect('add-student')
    course_list = Course.objects.all()
    return render(request, 'add_student.html', {'course_list': course_list})

def add_teacher(request):
    if request.method == "POST":
        teacher  = Teacher()
        teacher.teacher_name = request.POST["teacher-name"]
        teacher.date_of_birth = request.POST["date-of-birth"]
        teacher.gender = request.POST["gender"]
        teacher.religion = request.POST["religion"]
        teacher.contact_number = request.POST["contact-number"]
        teacher.email = request.POST["email"]
        teacher.qualifications = request.POST["qualifications"]
        teacher.address = request.POST["address"]
        teacher.status = request.POST["status"]
        teacher.save()
        messages.add_message(request, messages.SUCCESS, "Teacher add sucsessfully")
        return redirect('add-teacher')
    return render(request, 'add_teacher.html')

def add_course(request):
    if request.method == "POST":
        course  = Course()
        try:
            course.course_name = request.POST["course-name"]
            course.desc = request.POST["desc"]
            course.fee_type = request.POST["fee-type"]
            course.fee = request.POST["fee"]
            course.save()
            messages.add_message(request, messages.SUCCESS, "Course add sucsessfully")
        except:
            messages.add_message(request, messages.ERROR, "Form Is Not valid")
        return redirect('add-course')
        
    return render(request, 'add_course.html')

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'course_list.html', {'courses': courses})

def course_details(request, id):
    course = Course.objects.get(id=id)
    students = course.student_set.all()

    context = {
        'course': course,
        'students': students
    }
    return render(request, 'course_details.html', context)

def single_student(request, id):
    student = Student.objects.get(id=id)
    return render(request, 'single_student.html', {'student': student})

def custom_404(request):
    return render(request, '404.html', status=404)