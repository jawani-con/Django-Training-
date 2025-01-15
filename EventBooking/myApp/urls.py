from . import views
from django.urls import path

urlpatterns = [ 
    path('', views.home, name="home"),  
    path('admin/events', views.get_all_events, name='get_all_events'),
    path('admin/events', views.add_new_event, name='add_new_event'),
    path('admin/events/<int:event_id>', views.update_event, name='update_event'),
    path('admin/events/<int:event_id>', views.delete_event, name='delete_event'),
]