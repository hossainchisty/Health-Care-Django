from django.db import models
from django.utils import timezone
from hospital.models import Doctor

class Appointment(models.Model):
    choices_time = (
        ('morning','Morning'),
        ('evening', 'Evening')
    )
    name = models.CharField(max_length=120)
    phone = models.CharField(max_length=11)
    email = models.EmailField()
    doctors = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='doctors')
    date = models.DateField(default=timezone.now)
    time = models.CharField(choices=choices_time, max_length=10)
    extra_note = models.TextField(null=True,blank=True)

    
    class Meta:
        verbose_name_plural = "Appointment"

    def __str__(self):
        return f'{self.name} - {self.doctors.name}'