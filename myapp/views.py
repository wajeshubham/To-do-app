from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt

from myapp.models import ToDo


# Create your views here.

def home(request):
    new_events = ToDo.objects.all().order_by('-added_date')
    front_end_stuff = {
        'new_events': new_events,
    }
    return render(request, 'myapp/new_event.html', front_end_stuff)


@csrf_exempt
def new_event(request):
    event = request.POST.get('event')
    added_date = timezone.now()
    ToDo.objects.create(task=event, added_date=added_date)
    front_end_stuff = {'event': event,
                       'added_date': added_date}
    return HttpResponseRedirect("/")


@csrf_exempt
def delete_event(request, todo_id):
    ToDo.objects.get(id=todo_id).delete()
    return HttpResponseRedirect("/")  # it will redirect the response to given url
