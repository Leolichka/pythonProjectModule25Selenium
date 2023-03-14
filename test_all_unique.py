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


def test_all_unique():
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

   element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'tbody>tr>th>img')))

   images = pytest.driver.find_elements(By.CSS_SELECTOR, 'tbody>tr>th>img')
   pytest.driver.implicitly_wait(10)
   names = pytest.driver.find_elements(By.XPATH, '//*[@id="all_my_pets"]/table/tbody/tr/td[1]')
   pytest.driver.implicitly_wait(10)
   animal_types = pytest.driver.find_elements(By.XPATH, '//*[@id="all_my_pets"]/table/tbody/tr/td[2]')
   pytest.driver.implicitly_wait(10)
   ages = pytest.driver.find_elements(By.XPATH, '//*[@id="all_my_pets"]/table/tbody/tr/td[3]')
   # statistic = pytest.driver.find_elements(By.XPATH, '//*[@id="all_my_pets"]/table/tbody/tr/td[3]')

   # все строки таблицы
   r = pytest.driver.find_elements(By.XPATH, '//*[@id="all_my_pets"]/table/tbody/tr')
   # все столбцы таблицы
   c = pytest.driver.find_elements(By.XPATH, '//*[@id="all_my_pets"]/table/tbody/tr[1]/td')

   rc = len(r)
   cc = len(c)

   list_pets = []
   for i in range(2, rc+1):
      d = pytest.driver.find_element(By.XPATH, "//tr[" + str(i) +"]").text
      print(d)
      list_pets.append(d)
      all = list(list_pets)
      unique = list(set(list_pets))
      print(f'\n Список всех питомцев', all)
      print(f'\n Список уникальных питомцев', unique)
      if all == unique:
         print('\n Уникальны')
      else:
         print('\n Не все уникальны')




