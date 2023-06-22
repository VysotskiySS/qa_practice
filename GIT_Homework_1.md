## GIT Homework 1

Для выполнения задания у вас должен быть установлен для Windows - GitBash.
Создан аккаунт в GitHub

Все шаги сценария выполняйте в терминале GitBush, Terminal, в папке под гитом.

Как отправить ДЗ на проверку.
 1. Создайте текстоовый файл как в первом ДЗ по Terminal.
 2. Сценарий перенесите в этот файл.
 3. На против каждого действия - напишите команду в GitBash

Файл со сценарием и ссылку на свой гит хаб отправляйте менторам на проверку.

git config --global user.name "VysotskiySS"

git config --global user.email idgwynbleidd@gmail.com

### TXT
 1. Создать внешний репозиторий c названием TXT.
github.com - repositories - New - Repository name TXT - Add a README file - Create repository
 2. Клонировать репозиторий TXT на локальный компьютер.
 3. Внутри локального TXT создать файл “new.txt”.
cd TXT
touch new.txt

 4. Добавить файл под гит.
git add new.txt

 5. Закоммитить файл.
git commit -m "comment"

 6. Отправить файл на внешний GitHub репозиторий.
git push

 7. Отредактировать содержание файла “new.txt” - написать информацию о себе (ФИО, возраст, количество домашних животных, будущая желаемая зарплата). Всё написать в формате TXT.
nano new.txt

full name: Vysotskiy Sergey Sergeevich
age: 32
count home pets: 1
salary: 60000

 8. Отправить изменения на внешний репозиторий.
git commit -am "change file new.txt" && git push

 9. Создать файл preferences.txt
nano preferences.txt
 10. В файл preferences.txt” добавить информацию о своих предпочтениях (Любимый фильм, любимый сериал, любимая еда, любимое время года, сторона которую хотели бы посетить) в формате TXT.

film: Bicentennial Man
serial: Stargate SG-1
food: Khachapuri
season: Summer
side of the world: East Asia

 11. Создать файл sklls.txt добавить информацию о скиллах которые будут изучены на курсе в формате TXT
nano skills.txt

1. Базовая теория (Что такое тестирование, багрепорты, документация, виды, методы, направления тестирования и т.п.) SDLC, STLC.
2. Что такое клиент-серверная архитектура.
3. HTTP Методы запросов на сервер.
4. Коды ответов HTTP сервера.
5. Структуры HTTP запросов и ответов.
6. Что такое JSON, XML. Их структура.
7. Тестирование API через Postman (JS, автотесты API).
8. Снятие и чтение логов c внешнего сервера.
9. Снифинг http web трафика через Charles и Fiddler.
10. Dev Tools веб браузеров (Google Chrome, FireFox).
11. VPN. (Как работает, зачем нужен, как использовать, варианты инструментов)
12. Мобильное тестирование.
13. Особенность iOS, Android, гайдлайны.
14. Сборка iOS приложений на XCode. (У кого нет Mac компьютера, просто посмотрят)
15. Сборка Android приложений на Android Studio.
16. ADB (управление андройд девайсами).
17. Настройка прокси и vpn на iOS и Android.
18. Перехват (сниффинг) мобильного трафика через Charles и Fiddler на iOS и Android.
19. Командная строка (terminal) Linux (копирование, создание, просмотр, перемещение файлов на серверах без графического интерфейса)
20. Основы bash скриптинг, автоматизация рутинных задач на сервере.
21. Доступ к удалённым серверам.
22. Основы SQL (Create, Delete, Drop, Insert Into, Select, From, Where, Join).
23. База данных Postgres (установка, настройка и использование).
24. Нереляционная база данных Redis (установка, настройка и использование).
25. Нагрузочное тестирование в Jmeter.
26. Методология разработки Scrum.
27. Техники тест-дизайна (Классы эквивалентности, граничные значения, комбинаторные техники (Попарный, ортогональный, базовый выбор, каждый выбор), состояния и переходы)
28. Python. (Изучение основ. Создание клиент серверного приложения)

 12. Сделать коммит в одну строку.
git add . && git commit -m "comment"

 13. Отправить сразу 2 файла на внешний репозиторий.
git push

 14. На веб интерфейсе создать файл bug_report.txt.
repositories - TXT - Add file - Create new file - name new file - bug_report.txt - Commit changes

 15. Сделать Commit changes (сохранить) изменения на веб интерфейсе.
Commit changes

 16. На веб интерфейсе модифицировать файл bug_report.txt, добавить баг репорт в формате TXT.

id - PR1-B1
Summary - Кнопка “Оформить заказ” не реагирует на клик на странице оформления заказа.
Project - Web site shop.com
Version - 1.1
Severity - Blocker
Priority - ASAP
Status - Open
Author - Vysotskiy S
Assigned To - Ivanov I
Description:
  Precondition:
    1 - Зарегистрироваться на сайте shop.com
    2 - Авторизоваться на сайте
  Environment - MacOS BigSur v:11.2.3. Google Chrome v: 94.0.4606.71 (x86_64)
  Steps_to_reproduce:
    1 - Добавить товар в корзину
    2 - Зайти в корзину
    3 - Нажать на кнопку оформить заказ
  Actual_result - Кнопка “Оформить заказ” не реагирует на клик.
  Expected result - Пользователь перенаправляется на страницу оплаты (Биллинг)
Attachment - https://drive.google.com/...

 17. Сделать Commit changes (сохранить) изменения на веб интерфейсе.
 
 19. Синхронизировать внешний и локальный репозиторий TXT

git pull

### JSON

 4. Создать внешний репозиторий c названием JSON.

github.com -> repositories -> New -> Repository name JSON -> Add a README file -> Create repository

 5. Клонировать репозиторий JSON на локальный компьютер.

git clone https://github.com/VysotskiySS/JSON

 6. Внутри локального JSON создать файл “new.json”.

cd JSON

touch new.json

 7. Добавить файл под гит.

git add new.json

 8. Закоммитить файл.

git commit -m "new.json add"

 9. Отправить файл на внешний GitHub репозиторий.

git push

*авторизация через код или браузер

10. Отредактировать содержание файла “new.json” - написать информацию о себе (ФИО, возраст, количество домашних животных, будущая желаемая зарплата). Всё написать в формате JSON.

nano [new.json](https://github.com/VysotskiySS/JSON/blob/main/new.json "открыть new.json")

 11. Отправить изменения на внешний репозиторий.

git commit -m "change new.json"

git push

 12. Создать файл preferences.json

touch preferences.json

 13. В файл preferences.json добавить информацию о своих предпочтениях (Любимый фильм, любимый сериал, любимая еда, любимое время года, сторона которую хотели бы посетить) в формате JSON.

nano [preferences.json](https://github.com/VysotskiySS/JSON/blob/main/preferences.json "открыть preferences.json")

 14. Создать файл sklls.json добавить информацию о скиллах которые будут изучены на курсе в формате JSON

touch skills.json

nano [skills.json](https://github.com/VysotskiySS/JSON/blob/main/skills.json "открыть skills.json")

 15. Отправить сразу 2 файла на внешний репозиторий.

git add .

git commit -m "add preferences.json and skills.json"

git push

 16. На веб интерфейсе создать файл bug_report.json.

repositories - JSON -> Add file -> Create new file -> name new file -> bug_report.json -> Commit changes

 17. Сделать Commit changes (сохранить) изменения на веб интерфейсе.

Commit changes

 18. На веб интерфейсе модифицировать файл bug_report.json, добавить баг репорт в формате JSON.

[bug_report.json](https://github.com/VysotskiySS/JSON/blob/main/bug_report.json "открыть bug_report.json") - Edit this file

 19. Сделать Commit changes (сохранить) изменения на веб интерфейсе.

Commit changes

 20. Синхронизировать внешний и локальный репозиторий JSON

git pull
