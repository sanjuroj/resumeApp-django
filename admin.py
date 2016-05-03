from django.contrib import admin

# Register your models here.

from .models import *


admin.site.register((
    Basics,
    Profile,
    Job,
    JobHighlight,
    Volunteer,
    VolunteerHighlight,
    Education,
    Course,
    Award,
    Publication,
    Skill,
    SkillKeyword,
    Language,
    Interest,
    InterestKeyword,
    Reference,
    ))