"""Defines URL patterns for learning_logs."""
from django.urls import path, include
from . import views
app_name = 'learning_logs'
urlpatterns = [
	# Home page
	path('', views.index, name='index'),
	# Page that shows all topics.
	path('topics/', views.topics, name='topics'),
	# Detail page for a single topic.
	path('topics/<int:topic_id>/', views.topic, name='topic'),
	# Page for adding a new topic
	path('new_topic/', views.new_topic, name='new_topic'),
	# Page for adding a new entry
	path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
	# Page for editing an entry.
	path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
  path('todo/',include('todo.urls',namespace='todo')),
  path('chat/',include('chat.urls',namespace='chat')),
	path('connect/',include('connect.urls',namespace='connect')),
]