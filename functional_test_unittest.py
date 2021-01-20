from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitor(unittest.TestCase):
  def setUp(self): #測試前執行
    self.browser = webdriver.Firefox()
    self.browser.implicitly_wait(3)

  def tearDown(self): #測試後執行
    return self.browser.quit()

  def test_can_start_a_list_and_retrieve_it_later(self): #主要區段
    self.browser.get('http://localhost:8000') #User查看首頁

    self.assertIn('To-Do',self.browser.title) #User發現<網頁標題> & <標頭h1>有 "To-Do" 字樣
    head_text = self.browser.find_element_by_tag_name('h1').text
    self.assertIn('To-Do',head_text)

    # User看到待辦事項輸入方塊
    inputbox = self.browser.find_element_by_id('id_new_item')
    self.assertEqual(inputbox.get_attribute('placeholder'),'Enter a to-do item')

    # User輸入待辦事項
    inputbox.send_keys('Buy dinner')

    # User Click Enter Button & Page will show "1:Buy dinner" , which is a to-do list item.
    inputbox.send_keys(Keys.ENTER)

    table = self.browser.find_element_by_id('id_list_table')
    rows = table.find_elements_by_tag_name('tr') #所有行(ROW)
    self.assertTrue(
      any(row.text == '1:Buy dinner' for row in rows)
    )
    

    self.fail('Finish the Test!!')

if __name__ == '__main__':
  unittest.main(warnings='ignore')