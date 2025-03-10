from django.shortcuts import render, get_object_or_404, redirect
from .forms import ContactForm, JobApplicationForm, SubscriptionForm
from .models import Job, Achievements
from django.core.paginator import Paginator
from django.core.mail import send_mail
from django.contrib import messages
from django.core.mail import EmailMessage


# Email settings
EMAIL_HOST_USER = 'majidsakr86@gmail.com'
ADMIN_EMAIL = 'contact@ma-hb.com'

def home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()
            
            # Prepare email content
            subject = "New Contact Form Submission"
            message = f"Name: {contact.name}\nEmail: {contact.email}\nMessage: {contact.message}"
            from_email = EMAIL_HOST_USER
            to_email = ADMIN_EMAIL
            
            # Send email
            send_mail(subject, message, from_email, [to_email])
            
            # Add success message
            messages.success(request, "Your message has been sent successfully!")
            return redirect('success')
    else:
        form = ContactForm()
    
    return render(request, 'pages/home.html', {'form': form})

def jobs(request):
    job_list = Job.objects.all()
    paginator = Paginator(job_list, 6)  # Show 6 jobs per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'pages/jobs.html', {'page_obj': page_obj})

def course(request):
    course_list = Course.objects.all()
    paginator = Paginator(course_list, 6)  # Show 6 courses per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'pages/courses.html', {'page_obj': page_obj})

def achievements(request):
    achievements_list = Achievements.objects.all()
    paginator = Paginator(achievements_list, 6)  # Show 6 courses per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'pages/achievements.html', {'page_obj': page_obj})

def apply_for_job(request, job_id):
    job = get_object_or_404(Job, id=job_id)

    if request.method == 'POST':
        form = JobApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.job = job
            application.save()
            
            # Prepare email content
            subject = f"New Job Application for {job.name}"
            message = (
                f"Job Title: {job.name}\n"
                f"Applicant Name: {application.full_name}\n"
                f"Applicant Email: {application.email}\n"
                f"Phone: {application.phone}\n"
                f"Expected Salary: {application.expected_salary}\n"
                f"Work Hours: {application.work_hours}\n"
                f"Qualifications: {application.qualifications}\n"
                f"Applied On: {application.applied_on}\n"
            )
            from_email = EMAIL_HOST_USER
            to_email = ADMIN_EMAIL
            
            # Create the email
            email = EmailMessage(subject, message, from_email, [to_email])
            
            # Attach the CV file
            if application.cv_file:
                cv_path = application.cv_file.path
                email.attach_file(cv_path)
            
            # Send the email
            email.send()
            
            # Add success message
            messages.success(request, "Your job application has been submitted successfully!")
            return redirect('success')
    else:
        form = JobApplicationForm()
    
    return render(request, 'pages/apply.html', {'form': form, 'job': job})

def job_details(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    return render(request, 'pages/job_details.html', {'job': job})


def apply_for_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)

    if request.method == 'POST':
        form = CourseApplicationForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.course = course
            application.course_name = course.name
            application.save()

            # Prepare email content
            subject = f"New Course Application for {course.name}"
            message = (
                f"Course Name: {application.course_name}\n"
                f"Full Name: {application.full_name}\n"
                f"Email: {application.email}\n"
                f"Phone: {application.phone}\n"
                f"Date of Birth: {application.date_of_birth}\n"
                f"Gender: {application.get_gender_display()}\n"
                f"Education: {application.education}\n"
                f"Institution Name: {application.institution_name}\n"
                f"Country: {application.country}\n"
                f"State: {application.state}\n"
                f"Employment Status: {application.get_employment_status_display()}\n"
                f"Previous Experience: {application.previous_experience}\n"
                f"Learned About Course: {application.get_learned_about_course_display()}\n"
            )

            email = EmailMessage(
                subject,
                message,
                EMAIL_HOST_USER,
                [ADMIN_EMAIL]
            )

            # Send the email
            email.send()

            # Add success message
            messages.success(request, "Your course application has been submitted successfully!")
            return redirect('success')
        else:
            # Debug: Print the form errors to the console (optional)
            print(form.errors)
    else:
        form = CourseApplicationForm()

    return render(request, 'pages/apply_for_course.html', {'form': form, 'course': course})

def subscribe(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for subscribing!')
            return redirect('success')  # Or any page you want to redirect to
        else:
            messages.error(request, 'There was an error. Please try again.')
    else:
        form = SubscriptionForm()
    return render(request, 'base.html', {'form': form})

def custom_404(request, exception):
    return render(request, 'pages/404.html', status=404)

def success_view(request):
    return render(request, 'pages/success.html')

def achievement_detail(request, id):
    achievement = get_object_or_404(Achievements, id=id)
    return render(request, 'pages/achievement_detail.html', {'achievement': achievement})