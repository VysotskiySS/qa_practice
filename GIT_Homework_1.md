## GIT Homework 1

Для выполнения задания у вас должен быть установлен для Windows - GitBash.
Создан аккаунт в GitHub

Все шаги сценария выполняйте в терминале GitBush, Terminal, в папке под гитом.

Как отправить ДЗ на проверку.
 1. Создайте текстоовый файл как в первом ДЗ по Terminal.
 2. Сценарий перенесите в этот файл.
 3. На против каждого действия - напишите команду в GitBash

Файл со сценарием и ссылку на свой гит хаб отправляйте менторам на проверку.
```
git config --global user.name "VysotskiySS"
git config --global user.email idgwynbleidd@gmail.com
```
### TXT
 1. Создать внешний репозиторий c названием TXT.
```
github.com -> repositories -> New -> Repository name TXT -> Add a README file -> Create repository
```
 2. Клонировать репозиторий TXT на локальный компьютер.
```
 git clone https://github.com/VysotskiySS/JSON
```
 4. Внутри локального TXT создать файл “new.txt”.
```
cd TXT
touch new.txt
```
 5. Добавить файл под гит.
```
git add new.txt
```
 6. Закоммитить файл.
```
git commit -m "comment"
```
 7. Отправить файл на внешний GitHub репозиторий.
```
git push
```
 8. Отредактировать содержание файла “new.txt” - написать информацию о себе (ФИО, возраст, количество домашних животных, будущая желаемая зарплата). Всё написать в формате TXT.
```
nano [new.txt](https://github.com/VysotskiySS/TXT/blob/main/new.txt "открыть new.txt")
```
 8. Отправить изменения на внешний репозиторий.
```
git commit -am "change file new.txt" && git push
```
 9. Создать файл preferences.txt
```
nano [preferences.txt](https://github.com/VysotskiySS/TXT/blob/main/preferences.txt "открыть preferences.txt")
```
 10. В файл preferences.txt” добавить информацию о своих предпочтениях (Любимый фильм, любимый сериал, любимая еда, любимое время года, сторона которую хотели бы посетить) в формате TXT.

 11. Создать файл sklls.txt добавить информацию о скиллах которые будут изучены на курсе в формате TXT
```
nano [skills.txt](https://github.com/VysotskiySS/TXT/blob/main/skills.txt "открыть skills.txt")
```
 12. Сделать коммит в одну строку.
```
git add . && git commit -m "comment"
```
 13. Отправить сразу 2 файла на внешний репозиторий.
```
git push
```
 14. На веб интерфейсе создать файл bug_report.txt.
```
repositories -> TXT -> Add file -> Create new file -> name new file -> bug_report.txt -> Commit changes
```
 15. Сделать Commit changes (сохранить) изменения на веб интерфейсе.
```
Commit changes
```
 16. На веб интерфейсе модифицировать файл bug_report.txt, добавить баг репорт в формате TXT.

TXT -> [bug_report.txt](https://github.com/VysotskiySS/TXT/blob/main/bug_report.txt "открыть bug_report.txt") -> Edit this file

 18. Сделать Commit changes (сохранить) изменения на веб интерфейсе.
 
 19. Синхронизировать внешний и локальный репозиторий TXT
```
git pull
```
### JSON

 4. Создать внешний репозиторий c названием JSON.
```
github.com -> repositories -> New -> Repository name JSON -> Add a README file -> Create repository
```
 5. Клонировать репозиторий JSON на локальный компьютер.
```
git clone https://github.com/VysotskiySS/JSON
```
 6. Внутри локального JSON создать файл “new.json”.
```
cd JSON
touch new.json
```
 7. Добавить файл под гит.
```
git add new.json
```
 8. Закоммитить файл.
```
git commit -m "new.json add"
```
 9. Отправить файл на внешний GitHub репозиторий.
```
git push
```
*авторизация через код или браузер

10. Отредактировать содержание файла “new.json” - написать информацию о себе (ФИО, возраст, количество домашних животных, будущая желаемая зарплата). Всё написать в формате JSON.

nano [new.json](https://github.com/VysotskiySS/JSON/blob/main/new.json "открыть new.json")

 11. Отправить изменения на внешний репозиторий.
```
git commit -m "change new.json"
git push
```
 12. Создать файл preferences.json
```
touch preferences.json
```
 13. В файл preferences.json добавить информацию о своих предпочтениях (Любимый фильм, любимый сериал, любимая еда, любимое время года, сторона которую хотели бы посетить) в формате JSON.

nano [preferences.json](https://github.com/VysotskiySS/JSON/blob/main/preferences.json "открыть preferences.json")

 14. Создать файл sklls.json добавить информацию о скиллах которые будут изучены на курсе в формате JSON

touch skills.json
nano [skills.json](https://github.com/VysotskiySS/JSON/blob/main/skills.json "открыть skills.json")

 15. Отправить сразу 2 файла на внешний репозиторий.
```
git add .
git commit -m "add preferences.json and skills.json"
git push
```
 16. На веб интерфейсе создать файл bug_report.json.
```
repositories -> JSON -> Add file -> Create new file -> name new file -> bug_report.json -> Commit changes
```
 17. Сделать Commit changes (сохранить) изменения на веб интерфейсе.
```
Commit changes
```
 18. На веб интерфейсе модифицировать файл bug_report.json, добавить баг репорт в формате JSON.

JSON -> [bug_report.json](https://github.com/VysotskiySS/JSON/blob/main/bug_report.json "открыть bug_report.json") -> Edit this file

 19. Сделать Commit changes (сохранить) изменения на веб интерфейсе.
```
Commit changes
```
 20. Синхронизировать внешний и локальный репозиторий JSON
```
git pull
```
### XML

 21. Создать внешний репозиторий c названием XML.
 22. Клонировать репозиторий XML на локальный компьютер.
```
git clone https://github.com/VysotskiySS/XML
```
 23. Внутри локального XML создать файл “new.xml”.
```
cd XML
touch new.xml
```
 24. Добавить файл под гит.
```
git add new.xml
```
 25. Закоммитить файл.
```
git commit -m "new.xml add"
```
 26. Отправить файл на внешний GitHub репозиторий.
```
git push
```
 27. Отредактировать содержание файла “new.xml” - написать информацию о себе (ФИО, возраст, количество домашних животных, будущая желаемая зарплата). Всё написать в формате XML.

nano [new.xml](https://github.com/VysotskiySS/XML/blob/main/new.xml "открыть new.xml")

 28. Отправить изменения на внешний репозиторий.
```
git commit -am "modified: new.xml"
git push
```
 29. Создать файл preferences.xml
```
touch preferences.xml
```
 30. В файл preferences.xml добавить информацию о своих предпочтениях (Любимый фильм, любимый сериал, любимая еда, любимое время года, сторона которую хотели бы посетить) в формате XML.

nano [preferences.xml](https://github.com/VysotskiySS/XML/blob/main/preferences.xml "открыть preferences.xml")

 31. Создать файл sklls.xml добавить информацию о скиллах которые будут изучены на курсе в формате XML
```
nano [skills.xml](https://github.com/VysotskiySS/XML/blob/main/skills.xml "открыть skills.xml")
```
 32. Сделать коммит в одну строку.
```
git add . && git commit -m "comment"
```
 33. Отправить сразу 2 файла на внешний репозиторий.
```
git push
```
 34. На веб интерфейсе создать файл bug_report.xml.
```
Add file -> Create new file -> Name: bug_report.xml
```
 35. Сделать Commit changes (сохранить) изменения на веб интерфейсе.
```
Commit New File
```
 36. На веб интерфейсе модифицировать файл bug_report.xml, добавить баг репорт в формате XML.

XML -> [bug_report.xml](https://github.com/VysotskiySS/XML/blob/main/bug_report.xml "открыть bug_report.xml") -> Edit this file

 37. Сделать Commit changes (сохранить) изменения на веб интерфейсе.
```
Commit changes
```
 38. Синхронизировать внешний и локальный репозиторий XML
```
git pull
```
