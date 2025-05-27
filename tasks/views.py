# views.py

from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Event, Category, Participant
import re # Import regex for dynamic participant fields
from django.contrib import messages

def dashboard(request):
    
    today = timezone.localdate()
    now = timezone.localtime().time()

    # Get all events from the database
    all_events = Event.objects.all()

    # Calculate dashboard statistics
    total_events = all_events.count()
    upcoming_events = all_events.filter(date__gt=today).order_by('date', 'time')
    past_events = all_events.filter(date__lt=today).order_by('-date', '-time')
    
    # Events for today, ordered by time
    today_events = all_events.filter(date=today).order_by('time')

    upcoming_count = upcoming_events.count()
    past_count = past_events.count()
    total_participants = Participant.objects.count()

    # Determine which events to display based on the 'type' query parameter
    event_type = request.GET.get('type', 'today') # Default to 'today' if no type is specified
    
    events_to_display = []
    title = ""

    if event_type == 'total_events':
        events_to_display = all_events
        title = "All Events"
    elif event_type == 'upcoming':
        events_to_display = upcoming_events
        title = "Upcoming Events"
    elif event_type == 'past':
        events_to_display = past_events
        title = "Past Events"
    elif event_type == 'today':
        events_to_display = today_events
        title = "Today's Events"
    else:
        # Fallback for invalid types, show today's events
        events_to_display = today_events
        title = "Today's Events"

    context = {
        'total_participants': total_participants,
        'total_events': total_events,
        'upcoming_count': upcoming_count,
        'past_count': past_count,
        'events': events_to_display,
        'title': title,
    }
    return render(request, 'menu/dashboard.html', context)

def add_new(request):
    event = Event.objects.all() 
    categories = Category.objects.all()

    if request.method == 'POST':
        # Get form data
        name = request.POST.get('name')
        category_id = request.POST.get('category')
        date = request.POST.get('date')
        time = request.POST.get('time')
        location = request.POST.get('location')
        description = request.POST.get('description')

        try:
            # Check if a category ID was provided
            if not category_id:
                messages.error(request, 'Category is required.')
                return render(request, 'menu/add_new.html', {
                    'event': event,
                    'categories': categories,
                    'name': name,
                    'date': date,
                    'time': time,
                    'location': location,
                    'description': description,
                    'selected_category_id': category_id
                })

            # Retrieve the Category object
            try:
                category_instance = Category.objects.get(pk=category_id)
            except Category.DoesNotExist:
                messages.error(request, 'Selected category does not exist.')
                return render(request, 'menu/add_new.html', {
                    'event': event,
                    'categories': categories,
                    'name': name,
                    'date': date,
                    'time': time,
                    'location': location,
                    'description': description,
                    'selected_category_id': category_id
                })

            # Create the event first
            new_event = Event(
                name=name,
                category=category_instance,
                date=date,
                time=time,
                location=location,
                description=description
            )
            new_event.save()

            # Process participants
            participant_count = 0
            while True:
                participant_name = request.POST.get(f'participant_name_{participant_count}')
                participant_email = request.POST.get(f'participant_email_{participant_count}')
                
                if not participant_name or not participant_email:
                    break
                
                # Create participant
                Participant.objects.create(
                    event=new_event,
                    name=participant_name,
                    email=participant_email
                )
                participant_count += 1

            messages.success(request, 'Event and participants created successfully!')
            return redirect('dashboard')

        except Exception as e:
            messages.error(request, f'Error creating event: {str(e)}')
            return render(request, 'menu/add_new.html', {
                'event': event,
                'categories': categories,
                'name': name,
                'date': date,
                'time': time,
                'location': location,
                'description': description,
                'selected_category_id': category_id
            })

    return render(request, 'menu/add_new.html', {'event': event, 'categories': categories})


def event(request):
    # Get all categories for the dropdown
    # categories = Category.objects.all().order_by('name')
    return render(request, 'menu/event.html')