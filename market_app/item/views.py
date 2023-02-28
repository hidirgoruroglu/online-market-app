from django.shortcuts import render,redirect,get_object_or_404

from django.contrib.auth.decorators import login_required

from django.db.models.query import Q

from .models import Item,Category

from .forms import NewItemForm,EditItemForm

# Create your views here.

def items(request):
    items = Item.objects.filter(is_sold = False)
    categories = Category.objects.all()
    category_id = request.GET.get("category", 0)
    query = request.GET.get("query","")
    if query:
        items = items.filter(Q(name__icontains = query) | Q(description__icontains = query))
    if category_id:
        items = items.filter(category_id = category_id)
    context = dict(
        items = items,
        query = query,
        categories = categories,
        category_id = int(category_id),
        )

    return render(request,"item/items.html",context)


def detail_view(request, id):
    item = get_object_or_404(Item,pk = id)
    related_items = Item.objects.filter(category = item.category,is_sold = False).exclude(pk = id)[0:3]
    context = dict(item = item,related_items = related_items)
    return render(request,"item/detail.html",context)

@login_required(login_url="core:login_view")
def add_item_view(request):
    form = NewItemForm()
    if request.method == "POST":
        form = NewItemForm(request.POST,request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.created_by = request.user
            f.save()
            return redirect("item:detail_view",id = f.id)
        
    context = dict(form = form)
    return render(request,"item/add_item.html",context)

@login_required(login_url="core:login_view")
def edit_item_view(request, id):
    item = get_object_or_404(Item,id = id, created_by = request.user)
    form = EditItemForm(instance=item)
    if request.method == "POST":
        form = EditItemForm(request.POST,request.FILES,instance=item)
        if form.is_valid():
            form.save()
            return redirect("item:detail_view",id = item.id)
        
    context = dict(form = form,title = "Ürün Düzenle")
    return render(request,"item/add_item.html",context)

@login_required(login_url="core:login_view")
def delete_item_view(request,id):
    item = get_object_or_404(Item,id = id,created_by = request.user)
    item.delete()
    return redirect("dashboard:index")