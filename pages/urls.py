from django.urls import path
from . import views
from django.contrib.sitemaps.views import sitemap
from .sitemaps import JobSitemap, StaticViewSitemap, AchievementsSitemap

sitemaps = {
    'jobs': JobSitemap,
    'static': StaticViewSitemap,
    'achievements': AchievementsSitemap,
}

urlpatterns = [
    path('', views.home, name='home'),
    path('success/', views.success_view, name='success'),
    path('jobs/', views.jobs, name='jobs'),
    path('jobs/<int:job_id>/', views.job_details, name='job_details'),
    path('apply/<int:job_id>/', views.apply_for_job, name='apply_for_job'),
    path('achievements/', views.achievements, name='achievements'),
    path('achievements/<int:id>/', views.achievement_detail, name='achievement_detail'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('subscribe/', views.subscribe, name='subscribe'),
]
