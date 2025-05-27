import os
import django
from datetime import datetime, timedelta

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'event_management.settings')
django.setup()

from tasks.models import Category, Event, Participant

def test_add_event():
    try:
        # First, create a category if none exists
        category, created = Category.objects.get_or_create(
            name='Test Category'
        )
        print(f"Category {'created' if created else 'already exists'}")

        # Create an event
        event = Event.objects.create(
            name='Test Event',
            category=category,
            date=datetime.now().date(),
            time=datetime.now().time(),
            location='Test Location',
            description='Test Description'
        )
        print(f"Event created successfully: {event}")

        # Create a participant
        participant = Participant.objects.create(
            event=event,
            name='Test Participant',
            email='test@example.com'
        )
        print(f"Participant created successfully: {participant}")

    except Exception as e:
        print(f"Error occurred: {str(e)}")

if __name__ == '__main__':
    test_add_event() 