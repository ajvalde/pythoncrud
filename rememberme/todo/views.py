from django.shortcuts import render, get_object_or_404
from .models import Reminder
# Create your views here.

def list_of_post(request):
    rem = Reminder.objects.all()
    template = 'list_of_posts.html'
    context = {'rem': rem}
    return render(request, template, context)

def post_detail(request, id):
    rem = get_object_or_404(Reminder, id=id)
    template = 'singlepost.html'
    context = {'rem': rem}
    return render(request, template, context)
