from django.shortcuts import render

from .tasks import test_task
from django.http.response import HttpResponse

def test(request):
    test_task.delay()
    return HttpResponse("Completed")