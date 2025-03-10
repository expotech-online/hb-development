from django import forms
from .models import ContactMessage, JobApplication, Subscription

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'E-mail'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Tell us all about it',
                'rows': 4
            }),
        }


class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        exclude = ['job']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone'}),
            'expected_salary': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Expected Salary'}),
            'work_hours': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Work Hours'}),
            'cv_file': forms.FileInput(attrs={'class': 'form-control'}),
            'qualifications': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Qualifications for the Job', 'rows': 4}),
        }


class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = ['email']
