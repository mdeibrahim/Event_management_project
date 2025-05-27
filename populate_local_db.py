import os
import django
from datetime import datetime, timedelta
import random

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'event_management.settings')
django.setup()

from tasks.models import Category, Event, Participant

def populate_database():
    # Create categories
    categories = [
        Category.objects.create(name='Work'),
        Category.objects.create(name='Personal'),
        Category.objects.create(name='Social'),
        Category.objects.create(name='Education'),
        Category.objects.create(name='Health')
    ]
    print("Created categories")

    # Create events
    locations = ['New York', 'London', 'Paris', 'Tokyo', 'Sydney']
    for i in range(10):
        event = Event.objects.create(
            name=f'Event {i+1}',
            category=random.choice(categories),
            date=datetime.now().date() + timedelta(days=random.randint(-5, 10)),
            time=datetime.now().time(),
            location=random.choice(locations),
            description=f'Description for Event {i+1}'
        )
        
        # Create participants for each event
        for j in range(random.randint(1, 5)):
            Participant.objects.create(
                event=event,
                name=f'Participant {j+1} for Event {i+1}',
                email=f'participant{j+1}.event{i+1}@example.com'
            )
    
    print("Created events and participants")

if __name__ == '__main__':
    populate_database() 