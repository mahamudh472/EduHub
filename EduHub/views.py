from django.shortcuts import render, redirect
from main.models import Student, Course, Teacher, OneTimeFee, MonthlyFee, MONTHS
from django.contrib import messages 
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.utils import timezone
from django.shortcuts import get_object_or_404

@login_required(login_url='login')
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

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = User.objects.get(username=username)
        if user is not None:
            if user.check_password(password):
                authenticate(request, username=username, password=password)
                login(request, user)
                messages.add_message(request, messages.SUCCESS, "Login Successfully")
                return redirect('index')
            else:
                messages.add_message(request, messages.ERROR, "Password is incorrect")
                return redirect('login')
        else:
            messages.add_message(request, messages.ERROR, "Username is incorrect")
            return redirect('login')
    return render(request, 'login.html')
def logout_view(request):
    logout(request)
    messages.add_message(request, messages.SUCCESS, "Logout Successfully")
    return redirect('login')

def register(request):
    if request.method == "POST":
        first_name = request.POST["first-name"]
        last_name = request.POST["last-name"]
        email = request.POST["email"]
        username = request.POST["username"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm-password"]
        if password == confirm_password:
            user = User.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=username, password=password)
            user.save()
            messages.add_message(request, messages.SUCCESS, "Account created successfully")
            return redirect('login')
        else:
            messages.add_message(request, messages.ERROR, "Password and Confirm Password does not match")
            return redirect('register')
        
    return render(request, 'register.html')

def forgot_password(request):
    return render(request, 'forgot-password.html')

def student_list(request):
    students = Student.objects.all() 
    course_list = Course.objects.all()
    return render(request, 'students_list.html', {'students': students, 'course_list': course_list})

def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request, 'teacher_list.html', {"teachers": teachers})

def add_student(request):
    if request.method == "POST":
        try:
            student  = Student()
            student.student_photo = request.FILES["student-photo"] if request.FILES["student-photo"] else None
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
            student.student_id = student.course.student_set.last().student_id + 1 if student.course.student_set.last() else Course.objects.get(course_name=request.POST["course"]).first_roll
            student.save()
            if student.course.fee_type == 'one-time':
                payment = OneTimeFee.objects.create(student=student, name=student.student_name)
            
            if student.course.fee_type == 'monthly':
                for i in range(12):
                    payment = MonthlyFee.objects.create(student=student, month_name=MONTHS[i][0])
                    print(MONTHS[i][0])
            
            messages.add_message(request, messages.SUCCESS, "Student add sucsessfully")
            return redirect('add-student')
        except:
            messages.add_message(request, messages.ERROR, "Form Is Not valid")
            return redirect('add-student')
    course_list = Course.objects.all()
    return render(request, 'add_student.html', {'course_list': course_list})

def add_teacher(request):
    if request.method == "POST":
        try:
            teacher  = Teacher()
            teacher.teacher_photo = request.FILES["teacher-photo"] if request.FILES["teacher-photo"] else None
            teacher.teacher_name = request.POST["teacher-name"]
            teacher.teacher_position = request.POST["teacher-position"]
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
        except:
            messages.add_message(request, messages.ERROR, "Form Is Not valid")
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
            course.first_roll = request.POST["first-roll"]
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
def testimonial(request):
    return render(request, 'testimonial.html')

def custom_404(request, exceptions):
    return render(request, '404.html', status=404)
def single_teacher(request, id):
    teacher = Teacher.objects.get(id=id)
    return render(request, 'single_teacher.html', {'teacher': teacher})

def generate_pdf(request):
    students = Student.objects.all()
    context = {
        'students': students
    }
    return render(request, 'generate_pdf.html', context)

def payment(request):
    if request.method == "POST":
        id = request.POST.get('id')
        if id:
            try:
                student = Student.objects.filter(student_id=int(id))[0]
                months = student.monthlyfee_set.filter(status=False)
                if months.count() == 0:
                    status = "Paid"
                else:
                    status = "Unpaid"
                return render(request, 'payment.html', {'student': student, 'months': months, 'status': status})
            except:
                messages.add_message(request, messages.ERROR, "Form Is Not valid")
                return redirect('index')
        else:
            messages.add_message(request, messages.ERROR, "Student Not Found")
            return redirect('index')
    return render(request, 'payment.html')

def pay(request):
    if request.method == "POST":
        id = request.POST.get('id')
        if request.POST.get('fee-type') == 'one-time':
            student = get_object_or_404(Student, student_id=int(id))
            student.onetimefee.status = True
            student.onetimefee.save()
            messages.add_message(request, messages.SUCCESS, "Payment Successful")
            return redirect('index')
        else:
            student = get_object_or_404(Student, student_id=int(id))
            monthly_fee = student.monthlyfee_set.get(month_name=request.POST['month_name'])
            monthly_fee.status = True
            monthly_fee.save()

            messages.add_message(request, messages.SUCCESS, "Payment Successful")
            return redirect('index')
    return render(request, 'payment.html')