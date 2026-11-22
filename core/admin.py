from django.contrib import admin
from .models import (Certificate, ContactMessage, Education, Experience, Profile,
                     Project, Skill, SkillGroup, Stat)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return not Profile.objects.exists()  # only one profile


class SkillInline(admin.TabularInline):
    model = Skill
    extra = 3


@admin.register(SkillGroup)
class SkillGroupAdmin(admin.ModelAdmin):
    list_display = ("title", "order")
    list_editable = ("order",)
    inlines = [SkillInline]


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "order")
    list_editable = ("order",)


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ("role", "company", "period", "order")
    list_editable = ("order",)


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ("title", "institute", "period", "order")
    list_editable = ("order",)


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ("title", "issuer", "link", "order")
    list_editable = ("order",)


@admin.register(Stat)
class StatAdmin(admin.ModelAdmin):
    list_display = ("label", "value", "order")
    list_editable = ("order",)


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "created")
    readonly_fields = ("name", "email", "message", "created")

    def has_add_permission(self, request):
        return False
