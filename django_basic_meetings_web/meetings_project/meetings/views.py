from django.shortcuts import render, get_object_or_404, redirect
from django.forms import modelform_factory
from .models import Meetings, Room


# Show detailed info about meeting obj
def detail(request, id):
    meeting = get_object_or_404(Meetings, pk=id)
    return render(request, "meetings/detail.html", {"meeting": meeting})


def list_rooms(request):
    return render(request, "rooms/rooms_list.html", {"Rooms": Room.objects.all()})


# Generating new class based on Meetings
MeetingForm = modelform_factory(Meetings, exclude=[])


# Adding new meetings
def new(request):
    # Adding to DB if Post
    if request.method == "POST":
        form = MeetingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("welcome")
    # Else is Get
    else:
        form = MeetingForm()
    return render(request, "meetings/new.html", {"form": form})
