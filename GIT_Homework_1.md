GIT Homework 1

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


JSON
 4. Создать внешний репозиторий c названием JSON.
 5. 
github.com - repositories - New - Repository name JSON - Add a README file - Create repository

 5. Клонировать репозиторий JSON на локальный компьютер.
 6. 
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

repositories - JSON - Add file - Create new file - name new file - bug_report.json - Commit changes

 17. Сделать Commit changes (сохранить) изменения на веб интерфейсе.

Commit changes

 18. На веб интерфейсе модифицировать файл bug_report.json, добавить баг репорт в формате JSON.

[bug_report.json](https://github.com/VysotskiySS/JSON/blob/main/bug_report.json "открыть bug_report.json") - Edit this file

 19. Сделать Commit changes (сохранить) изменения на веб интерфейсе.

Commit changes

 20. Синхронизировать внешний и локальный репозиторий JSON

git pull
