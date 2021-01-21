from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class NewVisitorTest(LiveServerTestCase):
  def setUp(self):
    self.browser = webdriver.Firefox()
    self.browser.implicitly_wait(1)

  def tearDown(self):
    self.browser.quit()
  
  # def test_page_title_has_todo_wording(self):
  #   self.browser.get(self.live_server_url)
  #   self.assertIn('To-Do',self.browser.title)

  #   head_text = self.browser.find_element_by_tag_name('h1').text
  #   self.assertIn('To-Do',head_text)

  def test_can_start_a_list_and_retrieve_it_later(self): #主要區段
    self.browser.get(self.live_server_url)

    inputbox = self.browser.find_element_by_name('item_text')
    self.assertEqual(inputbox.get_attribute('placeholder'),'Enter a to-do item')

    inputbox.send_keys('Buy Dinner')
    inputbox.send_keys(Keys.RETURN)

    import time
    time.sleep(5)

    inputbox = self.browser.find_element_by_name('item_text')
    inputbox.send_keys('Go to Work')
    inputbox.send_keys(Keys.RETURN)

    time.sleep(10)
    
    table = None
    table = WebDriverWait(self.browser,10).until(
      EC.presence_of_element_located((By.ID , "id_list_table"))
    )

    if table != None:
      rows = table.find_elements_by_tag_name('tr')
      self.assertIn('Buy Dinner',[row.text for row in rows])
      self.assertIn('Go to beach',[row.text for row in rows])

    self.fail('Finish the Test!!')