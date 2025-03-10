from django.contrib import admin
from .models import ContactMessage, Job, JobApplication, Subscription, Achievements
from import_export.admin import ImportExportModelAdmin

@admin.register(ContactMessage)
class ContactAdmin(ImportExportModelAdmin):
    pass

@admin.register(Job)
class JobAdmin(ImportExportModelAdmin):
    pass

@admin.register(JobApplication)
class JobApplicationAdmin(ImportExportModelAdmin):
    pass


@admin.register(Subscription)
class SubscriptionAdmin(ImportExportModelAdmin):
    pass

@admin.register(Achievements)
class AchievementsAdmin(ImportExportModelAdmin):
    pass

admin.site.site_header = "HB Development administration"
