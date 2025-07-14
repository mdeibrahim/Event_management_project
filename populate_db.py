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

    # Create Categories (only allowed choices)
    allowed_categories = ['social', 'workshop', 'seminar', 'others']
    categories = []
    for name in allowed_categories:
        category, _ = Category.objects.get_or_create(name=name)
        categories.append(category)
    print(f"Ensured {len(categories)} categories.")

    # Create Events and Participants
    events = []

    for _ in range(50):  # Use a smaller number for testing, increase as needed
        # Generate a random date within the next 30 days
        event_date = fake.date_between(start_date='-10d', end_date='+30d')
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
        events.append(event)

        # Add random participants to the event
        for _ in range(random.randint(1, 5)):
            Participant.objects.create(
                event=event,
                name=fake.name(),
                email=fake.email()
            )
    
    print(f"Created {len(events)} events with participants.")
    print("Database populated successfully!")

if __name__ == '__main__':
    print("Starting database population...")
    populate_db()