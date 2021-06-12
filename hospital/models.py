from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=120)
    speciality = models.CharField(max_length=120)
    picture = models.ImageField(upload_to="doctors/")
    experience = models.TextField()
    
    twitter = models.CharField(max_length=120, blank=True, null=True)
    facebook = models.CharField(max_length=120, blank=True, null=True)
    instagram = models.CharField(max_length=120, blank=True, null=True)

    def __str__(self):
        return self.name

class Testimonial(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    image = models.ImageField(upload_to="feedback/")


