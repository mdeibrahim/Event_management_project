import os
import django
import dj_database_url

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'event_management.settings')
django.setup()

from tasks.models import Category, Event, Participant

def transfer_data():
    # Get all data from local database
    categories = Category.objects.all()
    events = Event.objects.all()
    participants = Participant.objects.all()

    # Print the data we're going to transfer
    print(f"Found {categories.count()} categories")
    print(f"Found {events.count()} events")
    print(f"Found {participants.count()} participants")

    # Update database URL to use Render database
    os.environ['DATABASE_URL'] = 'postgresql://task_management_db_dqbj_user:IeENJNhBlfW3jeJma5MqIlnhCM6A5yKX@dpg-d0qpjn95pdvs73aqoqsg-a.oregon-postgres.render.com/task_management_db_dqbj'
    
    # Clear existing data in remote database
    Participant.objects.all().delete()
    Event.objects.all().delete()
    Category.objects.all().delete()

    # Transfer categories
    for category in categories:
        Category.objects.create(
            name=category.name
        )
    print("Categories transferred")

    # Transfer events
    for event in events:
        Event.objects.create(
            name=event.name,
            category=Category.objects.get(name=event.category.name),
            date=event.date,
            time=event.time,
            location=event.location,
            description=event.description
        )
    print("Events transferred")

    # Transfer participants
    for participant in participants:
        Participant.objects.create(
            event=Event.objects.get(name=participant.event.name),
            name=participant.name,
            email=participant.email
        )
    print("Participants transferred")

if __name__ == '__main__':
    transfer_data() 