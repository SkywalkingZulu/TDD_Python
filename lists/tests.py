from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string

from lists.views import home_page

class HomePageTest(TestCase):   #繼承 django.test.TestCase 類別
  def test_root_url_resolves_to_home_page_view(self):
    found = resolve('/')
    self.assertEqual(found.func , home_page)

  def test_home_page_can_save_a_POST_request(self):
    request = HttpRequest()
    request.method = 'POST'
    request.POST['item_text'] = 'A new list item..'

    response = home_page(request)

    import time
    time.sleep(10)

    self.assertIn('A new list item..',response.content.decode())
    expected_html = render_to_string(
      'home.html',
      {'new_item_text':'A new list item..'}
    )
    self.assertEqual(response.content.decode() , expected_html)

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

