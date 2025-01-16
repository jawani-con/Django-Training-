from rest_framework.test import APITestCase
from rest_framework import status
from myApp.models import Event

class EventAPITests(APITestCase):

    def setUp(self):
        """Set up initial data for tests."""
        Event.objects.create(name="Test Event", description="A test event", date="2025-01-20T10:00:00Z")

    def test_get_all_events(self):
        """Test fetching all events."""
        response = self.client.get('/admin/events')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1) 
        self.assertEqual(response.data[0]['name'], "Test Event")

    def test_add_new_event(self):
        """Test adding a new event."""
        data = {
            "name": "New Event",
            "description": "This is a new event",
            "date": "2025-02-10T10:00:00Z"
        }
        response = self.client.post('/admin/events', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Event.objects.count(), 2)  
        self.assertEqual(Event.objects.last().name, "New Event")

    def test_update_event(self):
        """Test updating an existing event."""
        event = Event.objects.first()
        data = {
            "name": "Updated Event",
            "description": "Updated description",
            "date": "2025-01-22T15:00:00Z"
        }
        response = self.client.put(f'/admin/events/{event.id}', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        event.refresh_from_db()
        self.assertEqual(event.name, "Updated Event")

    def test_delete_event(self):
        """Test deleting an event."""
        event = Event.objects.first()
        response = self.client.delete(f'/admin/events/{event.id}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Event.objects.count(), 0)
