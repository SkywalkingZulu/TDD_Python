from django.shortcuts import render
from django.http import HttpResponse

# V2
def home_page(request):
  return render(request , 'home.html') #Django會在APP目錄內,自動尋找templates資料夾 & 顯示的範本(templates)名稱

# V1
# def home_page(request):
#   return HttpResponse('<html><title>To-Do lists</title></html>')

