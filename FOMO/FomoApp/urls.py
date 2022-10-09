from django.urls import path
from . import views

urlpatterns = [
    path('api/login/', views.login_request_view),
    path('api/logout/', views.logout), #done
    path('api/jsonActivityEvents/', views.jsonActivityEvents),#done
    path('api/jsonDeadlineEvents/', views.jsonDeadlineEvents), #done
    path('api/jsonDeadlines/', views.jsonDeadlines), #done
    path('api/activitesUpdate/', views.activitesUpdate), #done
    path('api/deadlineEventsUpdate/', views.deadlineEventsUpdate), #dobe
    path('api/createDeadlineEvents/', views.createDeadlineEvents), #done
    path('api/deleteDeadlineEvents/', views.deleteDeadlineEvents),
    path('api/getEvents/', views.getIcs), #done
    path('api/checkIcs/', views.checkIcs), #done
    path('api/saveUserDetails/', views.saveUserDetails), #done
    path('api/jsonUserDetails/', views.jsonUserDetails)
]