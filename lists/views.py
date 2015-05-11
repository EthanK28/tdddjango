from django.shortcuts import render, redirect
from django.http import HttpResponse
from lists.models import Item, List
from django.core.exceptions import ValidationError

# Create your views here.

def home_page(request):
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/lists/the-only-list-in-the-world')
        # new_item_text = request.POST['item_text']
        # Item.objects.create(text=new_item_text)
    items = Item.objects.all()
    return render(request, 'home.html')
    # else:
        #new_item_text = ''
    # item = Item()
    # item.text = request.POST.get('item_text', '')
    # item.save()

    # return render(request, 'home.html', {
    #     'new_item_text': new_item_text
    # })


def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)

    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'], list=list_)
        return redirect('/lists/%d/' % (list_.id, ))
    #items = Item.objects.filter(list=list_)

    return render(request, 'list.html', {'list': list_})

def new_list(request):
    list_ = List.objects.create()
    item = Item.objects.create(text=request.POST['item_text'], list=list_)


    try:
        item.full_clean()
        item.save()
        #item.save()
    except ValidationError:
        list_.delete()
        error = "You can't have an empty list item"
        return render(request, 'home.html', {"error": error})
        # return render(request, 'home.html')
        # pass
        #list_.delete()


    return redirect('/lists/%d/' % (list_.id, ))

    #return redirect('/lists/%d/' % (list_.id))

# def add_item(request, list_id):
#     list_ = List.objects.get(id=list_id)
#     Item.objects.create(text=request.POST['item_text'], list=list_)
#     return redirect('/lists/%d/' % (list_.id))


