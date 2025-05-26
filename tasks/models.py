from django.db import models

# Create your models here.
from django.db import models
from django.urls import reverse
# Create your models here.

class Category(models.Model):
    name = models.CharField(
        max_length=100,
        help_text="Enter a name for the category (e.g. 'Work', 'Personal', 'Other')"
    )
    description = models.TextField(
        blank=True,
        help_text="Enter a brief description of the category"
    )
    
    class Meta:
        verbose_name = "category"
        ordering = ["name"]

    def __str__(self):
        return self.name
    
class Event(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=200)
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        related_name="events"
    )

    class Meta:
        ordering = ['date', 'time']
        indexes = [
            models.Index(fields=['date']),
            models.Index(fields=['category'])
        ]

    def __str__(self):
        return f"{self.name} on {self.date} at {self.time}"
    
class Participant(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    events = models.ManyToManyField(
        Event,
        related_name="participants",
        blank=True
    )
    
    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name