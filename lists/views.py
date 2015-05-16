from django.shortcuts import render, redirect
from django.http import HttpResponse
from lists.models import Item, List
from lists.forms import ItemForm
from django.core.exceptions import ValidationError

# Create your views here.

def home_page(request):
    return render(request, 'home.html', {'form':ItemForm()})
    # if request.method == 'POST':
    #     Item.objects.create(text=request.POST['item_text'])
    #     return redirect('/lists/the-only-list-in-the-world')
    #
    #
    #     # new_item_text = request.POST['item_text']
    #     # Item.objects.create(text=new_item_text)
    # items = Item.objects.all()
    # return render(request, 'home.html')


    # else:
        #new_text = ''
    # item = Item()
    # item.text = request.POST.get('text', '')
    # item.save()

    # return render(request, 'home.html', {
    #     'new_text': new_item_text
    # })


def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    form = ItemForm()

    if request.method == 'POST':
        form = ItemForm(data=request.POST)
        if form.is_valid():
            Item.objects.create(text=request.POST['text'], list=list_)
            return redirect(list_)

    return render(request, 'list.html', {
        'list': list_, "form":form })

def new_list(request):
    form = ItemForm(data=request.POST)
    if form.is_valid():
        list_ = List.objects.create()
        Item.objects.create(text=request.POST['text'], list=list_)
        return redirect(list_)
    else:
        return render(request, 'home.html', {"form": form})

    # return redirect('/lists/%d/' % (list_.id, ))

    #return redirect('/lists/%d/' % (list_.id))

# def add_item(request, list_id):
#     list_ = List.objects.get(id=list_id)
#     Item.objects.create(text=request.POST['item_text'], list=list_)
#     return redirect('/lists/%d/' % (list_.id))


