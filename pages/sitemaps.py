from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Job, Achievements

class JobSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.8

    def items(self):
        return Job.objects.all()

    def lastmod(self, obj):
        return obj.created_at

class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'weekly'

    def items(self):
        return ['home', 'jobs', 'course']

    def location(self, item):
        return reverse(item)

class AchievementsSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.6

    def items(self):
        return Achievements.objects.all()

    def lastmod(self, obj):
        return obj.created_at