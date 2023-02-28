from django.shortcuts import render,redirect,get_object_or_404

from django.contrib.auth.decorators import login_required

from item.models import Item

# Create your views here.

@login_required(login_url="core:login_view")
def index(request):
    items = Item.objects.filter(created_by = request.user)
    context = dict(items = items)
    return render(request,"dashboard/index.html",context)

