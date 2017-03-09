from django.shortcuts import render, get_object_or_404
from .models import Remember
# Create your views here.

def list_of_post(request):
    rem = Remember.objects.all()
    template = 'list_of_posts.html'
    context = {'rem': rem}
    return render(request, template, context)

def post_detail(request, reminder_id):
    rem = get_object_or_404(Remember, reminder_id=reminder_id)
    template = 'post_detail.html'
    context = {'rem': rem}
    return render(request, template, context)

def new_reminder(request):
    template = 'new_reminder.html'
    return render(request, template)
