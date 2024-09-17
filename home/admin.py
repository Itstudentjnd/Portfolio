from django.contrib import admin
from .models import Contact, Project, ProjectImage

class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1

class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectImageInline]

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message', 'submitted_at')  # Display these fields in the admin panel
    search_fields = ('name', 'email')  # Add search functionality for name and email
    list_filter = ('submitted_at',)  # Filter by the submission date

admin.site.register(Project, ProjectAdmin)