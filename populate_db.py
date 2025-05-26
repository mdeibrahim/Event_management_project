import os
import django
from faker import Faker
import random
from datetime import timedelta

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'event_management.settings')
django.setup()

# Import models after Django setup
from tasks.models import Category, Event, Participant

def populate_db():
    # Initialize Faker
    fake = Faker()

    # Create Categories
    categories = [
        Category.objects.create(
            name=name,
            description=fake.paragraph()
        ) for name in ['Work', 'Personal', 'Social', 'Education', 'Health']
    ]
    print(f"Created {len(categories)} categories.")

    # Create Participants
    participants = [Participant.objects.create(
        name=fake.name(),
        email=fake.email()
    ) for _ in range(15)]
    print(f"Created {len(participants)} participants.")

    # Create Events
    events = []
    for _ in range(200):
        # Generate a random date within the next 30 days
        event_date = fake.date_between(start_date='-30d', end_date='+30d')
        # Generate a random time
        event_time = fake.time()
        # Generate a random location
        location = fake.address()
        
        event = Event.objects.create(
            name=fake.catch_phrase(),
            description=fake.paragraph(),
            date=event_date,
            time=event_time,
            location=location,
            category=random.choice(categories)
        )
        
        # Add random participants to the event
        event_participants = random.sample(participants, random.randint(1, 5))
        event.participants.set(event_participants)
        events.append(event)
    
    print(f"Created {len(events)} events.")
    print("Database populated successfully!")

if __name__ == '__main__':
    print("Starting database population...")
    populate_db()