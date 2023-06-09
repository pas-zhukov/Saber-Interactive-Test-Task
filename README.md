# Тестовое задание на вакансию «Junior Python Разработчик» в компании Saber Interactive

---

Полный текст тестового содержится в файле `Saber_Interactive_Junior_Python_Developer.docx`.

---
Программу можно скачать из командной строки:
``` 
git clone https://github.com/pas-zhukov/Saber-Interactive-Test-Task.git
```
*Для Windows необходимо предварительно установить [git](https://gitforwindows.org/), если он у Вас не установлен.*

### Установка зависимостей
Для корректной работы программы на вашем компьютере должен быть установлен интерпретатор [Python 3.9 или старше](https://www.python.org/downloads/), а также модули, перечисленные в файле `requirements.txt`.
Библиотеки можно установить при помощи pip:
```
pip install -r requirements.txt
```

### Запуск программы
Для запуска программы необходимо запустить консоль, перейти в папку с проектом, а затем перейти в папку `app`.
```
cd %path_to_project%/app
```
Для того, чтобы выполнить конкретную команду, используется следующий синтаксис:
```
python main.py [название_команды] <аргументы>
```
---

### Доступные команды
В качестве основных используются команды **list** и **get**.

Документацию к программе всегда можно просмотреть, используя следующую команду:
```
python main.py --help
```
### List
Команда **list** с аргументами _tasks_ или _builds_ выведет список загруженных задач или билдов соответственно. Например:
```
python main.py list builds
```
выведет в консоль:
```
List of available builds:
* approach_important
* audience_stand    
* time_alone
```
### Get
Команда **get** позволяет вывести подробную информацию о конкретной задаче или билде. **get** используется с двумя позиционными аргументами, первый соответствует выбору задач/билдов, второй уточняет имя конкретной задачи/билда. Например:
```
python main.py get task train_silver_centaurs
```
выведет в консоль:
```
Task info:
* name: train_silver_centaurs
* dependencies: design_black_centaurs, upgrade_blue_centaurs
```
_Если будет указано имя задачи/билда, которых не существует, программа выдаст ошибку_

### Изменение пути к файлам задач и билдов

По умолчанию программа ищет файлы tasks.yaml и builds.yaml в корневой папке. Чтобы указать другой путь к этим файлам, необходимо изменить глобальную переменную `PATH_TO_FILES` в файле `main.py':
```
PATH_TO_FILES = {
'tasks': '%путь_к_tasks.yaml%',
'builds: '%путь_к_builds.yaml%'
}
```
_Если путь будет некорректный, программа выдаст ошибку._

### Назначение программы и особенности реализации
Программа представляет из себя модель билд-системы с её базовым функционалом. Модель оперирует такими сущностями как "задача" и "билд", имеет методы для работы с этими сущностями.
CLI интерфейс реализован на базе модуля **click**. В отдельном файле описаны классы, методы и функции для описания задач, билдов, для десериализации yaml-файлов.
Программа разработана в рамках тестового задания на вакансию Junior Python разработчика.
