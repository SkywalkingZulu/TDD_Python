from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
import time

class NewVisitor(unittest.TestCase):
  def setUp(self): #測試前執行
    self.browser = webdriver.Firefox()
    self.browser.implicitly_wait(3)

  def tearDown(self): #測試後執行
    return self.browser.quit()

  # def check_for_row_in_list_table(self,row_text):
  #   # 沒有等待直接找,會報錯
  #   # table = self.browser.find_element_by_id('id_list_table') 
  #   table = WebDriverWait(self.browser , 20).until(
  #     EC.presence_of_element_located((By.ID , "id_list_table"))
  #   ) #Browser要等到Response回傳後,就可以找到了HTML element...^O^
  #   rows = table.find_elements_by_tag_name('tr')
  #   for row in rows:
  #     print(row.text)
  #   self.assertIn(row_text,[row.text for row in rows])

  def test_can_start_a_list_and_retrieve_it_later(self): #主要區段
    self.browser.get('http://localhost:8000') #User查看首頁

    # self.assertIn('To-Do',self.browser.title) #User發現<網頁標題> & <標頭h1>有 "To-Do" 字樣
    # head_text = self.browser.find_element_by_tag_name('h1').text
    # self.assertIn('To-Do',head_text)

    # # User看到待辦事項輸入方塊
    # inputbox = self.browser.find_element_by_id('id_new_item')
    # self.assertEqual(inputbox.get_attribute('placeholder'),'Enter a to-do item')

    # # User輸入待辦事項1
    # todo1 = 'Buy dinner'
    # inputbox.send_keys(todo1)
    # inputbox.send_keys(Keys.ENTER)
    # # self.check_for_row_in_list_table('Buy dinner')

    # wait = WebDriverWait(self.browser ,10)
    # table = wait.until(EC.element_to_be_selected((By.NAME,'list_table')),message='test')

    # # table = WebDriverWait(self.browser , 20).until(
    # #   EC.presence_of_element_located((By.NAME , "list_table"))
    # # ) #Browser要等到Response回傳後,就可以找到了HTML element...^O^
    
    # if table != None:
    #   rows = table.find_elements_by_tag_name('tr')
    #   for row in rows:
    #     print(row.text)
    #   self.assertIn(todo1,[row.text for row in rows])

    # # 除錯方式,在執行時,使用time.sleep來暫停測試
    # # time.sleep(5)
    # # # User輸入待辦事項2
    # # inputbox = self.browser.find_element_by_id('id_new_item')
    # # inputbox.send_keys('Go running')
    # # inputbox.send_keys(Keys.ENTER)
    # # self.check_for_row_in_list_table('Go running')

    self.fail('Finish the Test!!')

if __name__ == '__main__ ':
  unittest.main(warnings='ignore')