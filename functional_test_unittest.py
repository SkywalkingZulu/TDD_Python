from selenium import webdriver
import unittest

class NewVisitor(unittest.TestCase):
  def setUp(self): #測試前執行
    self.browser = webdriver.Firefox()
    self.browser.implicitly_wait(3)

  def tearDown(self): #測試後執行
    return self.browser.quit()

  def test_can_start_a_list_and_retrieve_it_later(self): #主要區段
    self.browser.get('http://localhost:8000')

    self.assertIn('To-Do',self.browser.title)

    self.fail('Finish the Test!!')

if __name__ == '__main__':
  unittest.main(warnings='ignore')