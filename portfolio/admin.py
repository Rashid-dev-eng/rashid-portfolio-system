from django.contrib import admin
from .models import Profile, Project


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("name", "title", "email")
    fieldsets = (("Identity", {"fields": ("name", "title", "availability")}), ("Hero", {"fields": ("hero_heading", "hero_text")}), ("About", {"fields": ("about_text", "about_detail", "about_image", "skills")}), ("Contact", {"fields": ("email", "phone", "whatsapp", "office")}), ("Social links", {"fields": ("tiktok_url", "facebook_url", "linkedin_url", "github_url", "instagram_url")}))


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "featured", "order")
    list_editable = ("featured", "order")
    list_filter = ("featured", "category")
    search_fields = ("title", "description")
