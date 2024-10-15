
from django.urls import path
from django.urls.conf import include
from . import views
urlpatterns = [
    path('send-mail/', views.send_mail_to_all, name="sendmail"),
    # path('schedulemail/', views.schedule_mail, name="schedulemail"),
]