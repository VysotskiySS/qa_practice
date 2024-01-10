import time

# webdriver это и есть набор команд для управления браузером
from selenium import webdriver

# импортируем класс By, который позволяет выбрать способ поиска элемента
from selenium.webdriver.common.by import By

# инициализируем драйвер браузера
driver = webdriver.Chrome()

# Метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
driver.get("https://nuxt-01.mp.lmdev.ru/")

# Задаем размер окна браузера
driver.set_window_size(1920, 1080)
time.sleep(5)

# Подтвердить бизнес регион
submit_button = driver.find_element(By.CSS_SELECTOR, ".btn-outline")
submit_button.click()
time.sleep(5)

# Разрешение на куки
submit_button = driver.find_element(By.CSS_SELECTOR, ".l-actions button:nth-child(1)")
submit_button.click()
time.sleep(5)

# РЕГИСТРАЦИЯ

# Нажать кнопку ЛК в Navbar
submit_button = driver.find_element(By.CSS_SELECTOR, "#AppNavbar div:nth-child(2) a:nth-child(2)")
submit_button.click()
time.sleep(5)

# Нажать кнопку "Зарегистрироваться"
submit_button = driver.find_element(By.XPATH, "//button[contains(., 'Зарегистрироваться')]")
submit_button.click()
time.sleep(5)

# Заполнить поле "E-mail"
textarea = driver.find_element(By.CSS_SELECTOR, "[type=email]")
textarea.send_keys("tester23n1@lime.auto")

# Заполнить поле "Телефон"
textarea = driver.find_element(By.CSS_SELECTOR, ".vti__input")
textarea.send_keys("9639447845")

# Заполнить поле "Имя"
textarea = driver.find_element(By.CSS_SELECTOR, "[placeholder='Ваше имя']")
textarea.send_keys("Ivanov")

# Заполнить поле "Фамилия"
textarea = driver.find_element(By.CSS_SELECTOR, "[placeholder='Фамилия']")
textarea.send_keys("Ivan")

# Заполнить поле "Пароль"
textarea = driver.find_element(By.CSS_SELECTOR, "[placeholder='Новый пароль']")
textarea.send_keys("Qwerty1")

# Заполнить поле "Повтор пароля"
textarea = driver.find_element(By.CSS_SELECTOR, "[placeholder='Повторите пароль']")
textarea.send_keys("Qwerty1")

# Выбрать чекбоксы подписок
click_chekbox = driver.find_element(By.CSS_SELECTOR, "[value='women'] ~.checkbox__indicator")
click_chekbox.click()

# Выбрать чекбокс "Согласия маркетинговых коммуникаций"
click_chekbox = driver.find_element(By.CSS_SELECTOR, ".FormGroup.mb-0 .checkbox__indicator")
click_chekbox.click()
time.sleep(5)

# Нажать кнопку "Зарегистрироваться"
click_chekbox = driver.find_element(By.CSS_SELECTOR, "[type='submit']")
click_chekbox.click()
time.sleep(5)

# находим элемент, содержащий текст
text_lk = driver.find_element(By.TAG_NAME, "h1")
# записываем в переменную текст из элемента
lk_text = text_lk.text

# с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
assert "ЛИЧНЫЙ КАБИНЕТ" == lk_text

# Закрыть окно браузера
driver.quit()
