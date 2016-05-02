from django.db import models
from django-phonenumber-field import PhoneNumberField

# Create your models here.

class Basics(models.Model):
    name = models.CharField(max_length=255)
    label = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone: PhoneNumberField()
    website = models.CharField(max_length=255)
    summary = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    postalCode = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    countryCode= models.CharField(max_length=255)
    region = models.CharField(max_length=255)
    
class Profile(models.Model):
  network = models.CharField(max_length=255)
  username = models.CharField(max_length=255)
  url = models.CharField(max_length=255)

class Job(models.model):
  company = models.CharField(max_length=255)
  position = models.CharField(max_length=255)
  website = models.CharField(max_length=255)
  startDate = models.DateField(max_length=255)
  endDate = models.DateField(max_length=255)
  summary = models.CharField(max_length=255)

class JobHighlight(models.Model):
  job = model.ForeignKey('Job',on_delete=models.CASCADE)
  highlight = models.TextField()

class Volunteer(models.Model):
  organization = models.CharField(max_length=255)
  position = models.CharField(max_length=255)
  website = models.CharField(max_length=255)
  startDate = models.DateField(max_length=255)
  endDate = models.DateField(max_length=255)
  summary = models.CharField(max_length=255)

class VolunteerHighlight(models.Model):
  volunteer = models.ForeignKey('Volunteer',on_delete=models.CASCADE)
  highlight = models.TextField(max_length=255)

class Education(models.Model):
  institution = models.CharField(max_length=255)
  area = models.CharField(max_length=255)
  studyType = models.CharField(max_length=255)
  startDate = models.DateField(max_length=255)
  endDate = models.DateField(max_length=255)
  gpa = models.DecimalField(max_length=255)

class Courses(models.Model):
  education = models.ForeignKey('Education',on_delete=models.CASCADE)
  course = models.CharField(max_length=255)

class Award(models.Model):
  title = models.CharField(max_length=255)
  date = models.DateField(max_length=255)
  awarder = models.CharField(max_length=255)
  summary = models.CharField(max_length=255)

class Publication(models.Model):
  name = models.CharField(max_length=255)
  publisher = models.CharField(max_length=255)
  releaseDate = models.DateField(max_length=255)
  website = models.CharField(max_length=255)
  summary = models.CharField(max_length=255)

class Award(models.Model):
  title = models.CharField(max_length=255)
  date = models.DateField(max_length=255)
  awarder = models.CharField(max_length=255)
  summary = models.CharField(max_length=255)

class Skill(models.Model):
  name = models.CharField(max_length=255)
  level = models.CharField(max_length=255)
  summary = models.CharField(max_length=255)

class SkillKeywords(models.Model):
  skill = models.ForeignKey('Skill',on_delete=models.CASCADE)
  keyword = models.CharField(max_length=255)

class Language(models.Model):
  name = models.CharField(max_length=255)
  level = models.CharField(max_length=255)

class Interest(models.Model):
  name = models.CharField(max_length=255)
  
class InterestKeywords(models.Model):
  interest = models.ForeignKey('Interest',on_delete=models.CASCADE)
  keyword = models.CharField(max_length=255)
  
class Reference(models.Model):
  name = models.CharField(max_length=255)
  reference = models.CharField(max_length=255)
  