from selenium.webdriver.common.by import By
from selenium import webdriver
import time
import pytest


@pytest.fixture(autouse=True)
def testing():
   pytest.driver = webdriver.Chrome('C:/Users/Olga/Documents/Test/chromedriver.exe')
   # Переходим на страницу авторизации
   pytest.driver.get('http://petfriends.skillfactory.ru/login')

   yield

   pytest.driver.quit()


def test_half_of_pets_have_photo():
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


   images = pytest.driver.find_elements(By.CSS_SELECTOR, 'tbody>tr>th>img')
   names = pytest.driver.find_elements(By.XPATH, '//*[@id="all_my_pets"]/table/tbody/tr/td[1]')
   animal_types = pytest.driver.find_elements(By.XPATH, '//*[@id="all_my_pets"]/table/tbody/tr/td[2]')
   ages = pytest.driver.find_elements(By.XPATH, '//*[@id="all_my_pets"]/table/tbody/tr/td[3]')

   count_photo = 0

   for i in range(len(images)):
      if images[i].get_attribute("src") != "":
         count_photo += 1
      else:
         count_photo +=0
         # print(f'Питомец {i} имеет пустое поле')
   print("\nКоличество загруженных фото питомцев: ", count_photo)

   count_pets = 0
   for i in range(len(images)):
      if images[i].get_attribute("src") == '' or images[i].get_attribute("src") != '':
         count_pets += 1
      # else:
      #    count_pets +=1
         # print(f'Питомец {i} имеет пустое поле')
   print("Количество питомцев: ", count_pets)

   # Находим половину от количества питомцев
   half = count_pets // 2

   # Проверяем что количество питомцев с фотографией больше или равно половине количества питомцев
   if count_photo >= half:
      print(f'количество фото: {count_photo}')
      print(f'Половина от числа питомцев: {half}')
   else:
      print(f'Питомцев с фото ({count_photo}) меньше половины от всех питомцев ({count_pets})')








