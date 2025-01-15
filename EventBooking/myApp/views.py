from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json
from .models import Event

@csrf_exempt
def get_all_events(request):
    if request.method == 'GET':
        events = Event.objects.all().values()
        return JsonResponse({'events': list(events)}, safe=False)

@csrf_exempt
def add_new_event(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        event = Event.objects.create(
            name=data.get('name'),
            description=data.get('description'),
            date=data.get('date')
        )
        return JsonResponse({'message': 'Event created', 'event_id': event.id}, status=201)

@csrf_exempt
def update_event(request, event_id):
    if request.method == 'PUT':
        data = json.loads(request.body)
        try:
            event = Event.objects.get(id=event_id)
            event.name = data.get('name', event.name)
            event.description = data.get('description', event.description)
            event.date = data.get('date', event.date)
            event.save()
            return JsonResponse({'message': 'Event updated'})
        except Event.DoesNotExist:
            return JsonResponse({'error': 'Event not found'}, status=404)

@csrf_exempt
def delete_event(request, event_id):
    if request.method == 'DELETE':
        try:
            event = Event.objects.get(id=event_id)
            event.delete()
            return JsonResponse({'message': 'Event deleted'})
        except Event.DoesNotExist:
            return JsonResponse({'error': 'Event not found'}, status=404)

def home(request):
     context={}
     return render(request, "myApp/home.html", context)

