from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Event
from .serializers import EventSerializer

@api_view(['GET'])
def get_all_events(request):
    events = Event.objects.all()
    serializer = EventSerializer(events, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def add_new_event(request):
    serializer = EventSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'Event created successfully'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_event(request, event_id):
    try:
        event = Event.objects.get(id=event_id)
    except Event.DoesNotExist:
        return Response({'error': 'Event not found'}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = EventSerializer(event, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'Event updated successfully'})
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_event(request, event_id):
    try:
        event = Event.objects.get(id=event_id)
        event.delete()
        return Response({'message': 'Event deleted successfully'})
    except Event.DoesNotExist:
        return Response({'error': 'Event not found'}, status=status.HTTP_404_NOT_FOUND)
