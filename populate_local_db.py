import os
import django
from datetime import datetime, timedelta
import random
from faker import Faker

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'event_management.settings')
django.setup()

from tasks.models import Category, Event, Participant

def populate_database():
    fake = Faker()
    
    # Create categories with descriptions
    categories = [
        Category.objects.create(name='Business Conference'),
        Category.objects.create(name='Workshop'),
        Category.objects.create(name='Networking Event'),
        Category.objects.create(name='Seminar'),
        Category.objects.create(name='Team Building'),
        Category.objects.create(name='Product Launch'),
        Category.objects.create(name='Training Session'),
        Category.objects.create(name='Hackathon')
    ]
    print("Created categories")

    # Create events
    locations = [
        'New York City, NY',
        'London, UK',
        'Tokyo, Japan',
        'Sydney, Australia',
        'Paris, France',
        'Berlin, Germany',
        'Singapore',
        'Dubai, UAE',
        'San Francisco, CA',
        'Toronto, Canada'
    ]

    event_types = [
        'Annual', 'Quarterly', 'Monthly', 'Weekly', 'Special',
        'International', 'Regional', 'Local', 'Virtual', 'Hybrid'
    ]

    for i in range(20):  # Create 20 events
        # Generate a random date between 30 days ago and 60 days in the future
        event_date = fake.date_between(start_date='-30d', end_date='+60d')
        # Generate a random time
        event_time = fake.time()
        
        event = Event.objects.create(
            name=f"{random.choice(event_types)} {fake.catch_phrase()}",
            category=random.choice(categories),
            date=event_date,
            time=event_time,
            location=random.choice(locations),
            description=fake.paragraph(nb_sentences=5)
        )
        
        # Create 3-8 participants for each event
        num_participants = random.randint(3, 8)
        for j in range(num_participants):
            Participant.objects.create(
                event=event,
                name=fake.name(),
                email=fake.email()
            )
    
    print(f"Created {Event.objects.count()} events")
    print(f"Created {Participant.objects.count()} participants")

if __name__ == '__main__':
    # Clear existing data
    Participant.objects.all().delete()
    Event.objects.all().delete()
    Category.objects.all().delete()
    
    # Populate with new data
    populate_database() 