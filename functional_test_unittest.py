from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest

class NewVisitor(unittest.TestCase):
  def setUp(self): #測試前執行
    self.browser = webdriver.Firefox()
    self.browser.implicitly_wait(3)

  def tearDown(self): #測試後執行
    return self.browser.quit()

  def check_for_row_in_list_table(self,row_text):
    # 沒有等待直接找,會報錯
    # table = self.browser.find_element_by_id('id_list_table') 
    table = WebDriverWait(self.browser , 20).until(
      EC.presence_of_element_located((By.ID , "id_list_table"))
    ) #Browser要等到Response回傳後,就可以找到了HTML element...^O^
    rows = table.find_elements_by_tag_name('tr')
    self.assertIn(row_text,[row.text for row in rows])

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
    
    # 除錯方式,在執行時,使用time.sleep來暫停測試
    import time
    time.sleep(5)

    self.check_for_row_in_list_table('Buy dinner')
    self.check_for_row_in_list_table('Go running')

    self.fail('Finish the Test!!')

if __name__ == '__main__':
  unittest.main(warnings='ignore')