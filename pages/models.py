from django.db import models
from django.urls import reverse
from django.utils import timezone


class ContactMessage(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} - {self.email}"

class Job(models.Model):
    JOB_TYPE_CHOICES = [
        ('remote', 'Remote'),
        ('onsite', 'On-site'),
        ('hybrid', 'Hybrid'),
    ]

    JOB_TIME_CHOICES = [
        ('fulltime', 'Full-Time'),
        ('parttime', 'Part-Time'),
    ]

    name = models.CharField(max_length=255)  
    description = models.TextField()  
    experience_required = models.CharField(max_length=20)  
    seniority_level = models.CharField(max_length=50) 
    employment_type = models.CharField(max_length=10, choices=JOB_TIME_CHOICES, default='fulltime')  # Employment type
    location = models.CharField(max_length=255)  
    role_overview = models.TextField(null=True, blank=True) 
    duties_responsibilities = models.TextField(null=True, blank=True)  
    job_type = models.CharField(max_length=10, choices=JOB_TYPE_CHOICES)  
    job_time = models.CharField(max_length=10, choices=JOB_TIME_CHOICES) 
    created_at = models.DateTimeField(default=timezone.now)
    
    # SEO Fields
    meta_description = models.CharField(max_length=160, null=True, blank=True)
    meta_keywords = models.CharField(max_length=255, null=True, blank=True)
    og_title = models.CharField(max_length=255, null=True, blank=True)
    og_description = models.CharField(max_length=255, null=True, blank=True)
    og_image = models.ImageField(upload_to='seo_images/', null=True, blank=True)
    og_type = models.CharField(max_length=50, default='article')

    def get_absolute_url(self):
        return reverse('apply_for_job', args=[self.id])

    def __str__(self):
        return self.name

class JobApplication(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='applications')
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    expected_salary = models.DecimalField(max_digits=10, decimal_places=2)
    work_hours = models.CharField(max_length=50)
    cv_file = models.FileField(upload_to='cv_files/')
    qualifications = models.TextField()
    applied_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Application for {self.job.name} from {self.full_name} - {self.email}"
    

class Achievements(models.Model):
    image = models.ImageField(upload_to='achievements_images/', null=True, blank=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    link = models.URLField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    
    # SEO Fields
    meta_description = models.CharField(max_length=160, null=True, blank=True)
    meta_keywords = models.CharField(max_length=255, null=True, blank=True)
    og_title = models.CharField(max_length=255, null=True, blank=True)
    og_description = models.CharField(max_length=255, null=True, blank=True)
    og_image = models.ImageField(upload_to='seo_images/', null=True, blank=True)
    og_type = models.CharField(max_length=50, default='article')

    def get_absolute_url(self):
        return reverse('achievement_detail', args=[str(self.id)])

    def __str__(self):
        return self.name
    


class Subscription(models.Model):
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
    