from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string

from lists.views import home_page
from lists.models import Item

class HomePageTest(TestCase):   #繼承 django.test.TestCase 類別
  def test_root_url_resolves_to_home_page_view(self):
    found = resolve('/')
    self.assertEqual(found.func , home_page)

  def test_home_page_only_saves_items_when_necessary(self):
    request = HttpRequest()
    home_page(request)
    self.assertEqual(Item.objects.count(),0)

  def test_home_page_can_save_a_POST_request(self):
    request = HttpRequest()
    request.method = 'POST'
    request.POST['item_text'] = 'A new list item..'

    response = home_page(request)

    self.assertEqual(Item.objects.count(),1)
    new_item = Item.objects.first()
    self.assertEqual(new_item.text,'A new list item..')
  
  def test_home_page_redirects_after_POST(self):
    request = HttpRequest()
    request.method = 'POST'
    request.POST['item_text'] = 'A new list item..'

    response = home_page(request)
    
    # 儲存後,應重新導回首頁
    self.assertEqual(response.status_code,302) #302=重新導向
    self.assertEqual(response['location'],'/')

  def test_home_page_displays_all_list_items(self):
    Item.objects.create(text='item 1')
    Item.objects.create(text='item 2')

    request = HttpRequest()
    response = home_page(request)

    self.assertIn('item 1',response.content.decode())
    self.assertIn('item 2',response.content.decode())


    # import time
    # time.sleep(10)

    # self.assertIn('A new list item..',response.content.decode()) #測試1:直接找response內容是否有'A new list item..'
    # expected_html = render_to_string(
    #   'home.html',
    #   {'new_item_text':'A new list item..'} #測試2:將HTML轉成Python字串後,再和response內容比較
    # )
    # self.assertEqual(response.content.decode() , expected_html)

class ItemModelTest(TestCase):
  def test_saving_and_retrieving_items(self):
    first_item = Item()
    first_item.text = 'The first (ever) list item'
    first_item.save()

    second_item = Item()
    second_item.text = 'Item the second'
    second_item.save()

    saved_items = Item.objects.all()
    self.assertEqual(saved_items.count(),2)

    first_saved_item = saved_items[0]
    second_saved_item = saved_items[1]
    self.assertEqual(first_saved_item.text , 'The first (ever) list item')
    self.assertEqual(second_saved_item.text , 'Item the second')

# V2 , (重構)binary位元組轉為Python字串再比較 , response.content.decode() &　render_to_string('home.html')
  # def test_home_page_returns_correct_html(self):
  #   request = HttpRequest()
  #   response = home_page(request)
  #   expected_html = render_to_string('home.html')
  #   self.assertEqual(response.content.decode() , expected_html)
    
# V1 , 直接用binary位元組作比較
  # def test_home_page_returns_correct_html(self):
  #   request = HttpRequest()
  #   response = home_page(request)
  #   self.assertTrue(response.content.startswith(b'<html>'))
  #   self.assertIn(b'<title>To-Do lists</title>',response.content)
  #   self.assertTrue(response.content.endswith(b'</html>'))

# V0
# class SmokeTest(TestCase):
#   def test_bad_math(self):
#     self.assertEqual(1+1 , 3 , "兩者不相等")

