from django.shortcuts import render , redirect
from django.http import HttpResponse
from lists.models import Item

# V2
def home_page(request):
  if request.method == 'POST':
    new_item_text = request.POST['item_text']
    Item.objects.create(text = new_item_text) #存入DB
    return redirect('/')
  
  items = Item.objects.all()
  return render(request , 'home.html' , {'items':items})
    #Notice:後端要用name='item_text'抓request內的值,而不是用id='id_new_item'抓
    #Django會在APP目錄內,自動尋找templates資料夾 & 顯示的範本(templates)名稱

# V1
# def home_page(request):
#   return HttpResponse('<html><title>To-Do lists</title></html>')

