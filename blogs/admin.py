from django.contrib import admin
from .models import Post, Comment, Category
from import_export.admin import ImportExportModelAdmin

@admin.register(Category)
class CategoryAdmin(ImportExportModelAdmin):
    pass

@admin.register(Post)
class PostAdmin(ImportExportModelAdmin):
    pass

admin.site.register(Comment)
admin.site.site_header = "LGS ASSURANCE administration"
