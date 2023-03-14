from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pytest


@pytest.fixture(autouse=True)
def testing():
   pytest.driver = webdriver.Chrome('C:/Users/Olga/Documents/Test/chromedriver.exe')
   # Переходим на страницу авторизации
   pytest.driver.get('http://petfriends.skillfactory.ru/login')

   yield

   pytest.driver.quit()


def test_all_pets_are():
   # Вводим email
   pytest.driver.find_element(By.ID, 'email').send_keys('leolichka@mail.ru')
   # Вводим пароль
   pytest.driver.find_element(By.ID, 'pass').send_keys('!@#456')
   # Нажимаем на кнопку входа в аккаунт
   pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

   # Проверяем, что мы оказались на главной странице пользователя
   assert pytest.driver.find_element(By.TAG_NAME, 'h1').text == "PetFriends"
   # time.sleep(5)  # just for demo purposes, do NOT repeat it on real projects!
   # Нажимаем на кнопку Мои питомцы
   pytest.driver.find_element(By.CSS_SELECTOR, 'a[class="nav-link"]').click()


   element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//div[@class=".col-sm-4 left"]')))
   element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".table.table-hover tbody tr")))

   images = pytest.driver.find_elements(By.CSS_SELECTOR, 'tbody>tr>th>img')
   names = pytest.driver.find_elements(By.XPATH, '//*[@id="all_my_pets"]/table/tbody/tr/td[1]')
   animal_types = pytest.driver.find_elements(By.XPATH, '//*[@id="all_my_pets"]/table/tbody/tr/td[2]')
   ages = pytest.driver.find_elements(By.XPATH, '//*[@id="all_my_pets"]/table/tbody/tr/td[3]')
   statistic = pytest.driver.find_element(By.XPATH, '//div[@class=".col-sm-4 left"]').text
   statistic = int(statistic.split('\n')[1].split(': ')[1])
   print(f'\n Количество питомцев в Статистике: ', statistic)


   count_pets = 0
   for i in range(len(images)):
      if images[i].get_attribute("src") == '' or images[i].get_attribute("src") != '':
         count_pets += 1
   print("Количество питомцев: ", count_pets)

   if statistic == count_pets:
       print('Количество питомцев в статистике соответствует количеству питомцев.')
   else:
       print('Bug')












