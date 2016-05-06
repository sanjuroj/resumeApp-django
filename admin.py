from django.contrib import admin

# Register your models here.

from .models import *

class JobHighlightInline(admin.TabularInline):
    model = JobHighlight

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    inlines = [
        JobHighlightInline
    ]
    

class VolunteerHighlightInline(admin.StackedInline):
    model = VolunteerHighlight

@admin.register(Volunteer)
class VolunteerAdmin(admin.ModelAdmin):
    inlines = [
        VolunteerHighlightInline
    ]


class CourseInline(admin.TabularInline):
    model = Course

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    inlines = [
        CourseInline
    ]


class SkillKeywordInline(admin.StackedInline):
    model = SkillKeyword

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    inlines = [
        SkillKeywordInline
    ]


class InterestKeywordInline(admin.StackedInline):
    model = InterestKeyword

@admin.register(Interest)
class InterestAdmin(admin.ModelAdmin):
    inlines = [
        InterestKeywordInline
    ]


admin.site.register((
    Basics,
    Profile,
    Award,
    Publication,
    Language,
    Reference,
))


