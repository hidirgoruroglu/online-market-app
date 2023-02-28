from django.shortcuts import redirect, render

from item.models import Category,Item
from .forms import RegisterForm
# Create your views here.
def index(request):
    items = Item.objects.filter(is_sold = False)[0:6]
    categories = Category.objects.all()
    context = dict(items = items,categories = categories)
    return render(request,"core/index.html",context)


def register_view(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        form.save()
        return redirect("core:login_view")
    

    context = dict(form = form)
    return render(request,"core/register.html",context)

def contact_view(request):
    return render(request,"core/contact.html")