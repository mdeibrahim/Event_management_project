# models.py

from django.db import models

class Category(models.Model):
    """
    Represents a category for events.
    """
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = "Categories" # Correct pluralization in admin

    def __str__(self):
        return self.name

class Event(models.Model):
    """
    Represents an event with details like name, category, date, time, location, and description.
    """
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=255)
    description = models.TextField()
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['date', 'time'] # Order events by date and time by default

    def __str__(self):
        return f"{self.name} on {self.date.strftime('%Y-%m-%d')} at {self.time.strftime('%H:%M')}"

class Participant(models.Model):
    """
    Represents a participant registered for a specific event.
    """
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='participants')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    registered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.email}) for {self.event.name}"
