from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Category, Event, Participant
from datetime import datetime, date

# Create your views here.
def dashboard(request):
    type = request.GET.get('type', 'today')
    
    # Get all events for the dashboard
    events = Event.objects.all().order_by('date', 'time')
    total_events = events.count()
    
    # Get today's date for filtering
    today = date.today()
    
    # Get events for different time periods
    upcoming_events = events.filter(date__gt=today)
    past_events = events.filter(date__lt=today)
    today_events = events.filter(date=today)
    
    # Get counts
    upcoming_count = upcoming_events.count()
    past_count = past_events.count()
    today_count = today_events.count()
    total_participants = Participant.objects.all().count()

    # Set display events based on type
    if type == 'upcoming':
        display_events = upcoming_events
        title = 'Upcoming Events'
    elif type == 'past':
        display_events = past_events
        title = 'Past Events'
    elif type == 'total_events':
        display_events = events
        title = 'All Events'
    else:
        display_events = today_events
        title = "Today's Events"

    context = {
        'events': display_events,
        'total_events': total_events,
        'upcoming_count': upcoming_count,
        'past_count': past_count,
        'today_count': today_count,
        'total_participants': total_participants,
        'title': title,
        'current_type': type
    }
    return render(request, 'menu/dashboard.html', context)

def event(request):
    # Get all categories for the dropdown
    categories = Category.objects.all().order_by('name')
    return render(request, 'menu/event.html', {'categories': categories})
    # return render(request, 'menu/event.html')

def add_new(request):
    if request.method == 'POST':
        # Get form data
        name = request.POST.get('name')
        category = request.POST.get('category')
        date = request.POST.get('date')
        time = request.POST.get('time')
        location = request.POST.get('location')
        description = request.POST.get('description')
        
        # TODO: Add your event creation logic here
        # For now, just redirect to events page
        messages.success(request, 'Event created successfully!')
        return redirect('event')
        
    return render(request, 'menu/add_new.html')

