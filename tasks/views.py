from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
def dashboard(request):
    return render(request, 'menu/dashboard.html')

def event(request):
    return render(request, 'menu/event.html')

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

