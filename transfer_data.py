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
    
    # Create a mapping of existing categories
    category_map = {}
    for category in categories:
        remote_category, created = Category.objects.get_or_create(
            name=category.name
        )
        category_map[category.id] = remote_category
    print("Categories transferred")

    # Create a mapping of existing events
    event_map = {}
    for event in events:
        remote_event, created = Event.objects.get_or_create(
            name=event.name,
            defaults={
                'category': category_map[event.category.id],
                'date': event.date,
                'time': event.time,
                'location': event.location,
                'description': event.description
            }
        )
        event_map[event.id] = remote_event
    print("Events transferred")

    # Transfer participants
    for participant in participants:
        Participant.objects.get_or_create(
            event=event_map[participant.event.id],
            name=participant.name,
            email=participant.email
        )
    print("Participants transferred")

if __name__ == '__main__':
    transfer_data() 