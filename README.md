![b3a5a00f-6e6b-488f-9ac1-5623c31cb0d1.jpg](design_tools%2Fb3a5a00f-6e6b-488f-9ac1-5623c31cb0d1.jpg)

# <p align="center"> Проект 3 </p>


## <p align="center">Описание</p>

**<p align="center">Проект 3 - это программа для взаимодействия с API сервиса HH и вывода информации о работодателях и их вакансиях</p>**

---

## <p align="center">Функции программы</p>


- **Вывод информации о работодателях**
- **Вывод информации о вакансиях**
- **Вывод средней зарплаты по вакансиям из БД**
- **Вывод вакансий с зарплатой выше среднего**
- **Вывод вакансий по ключевому слову**



----

## <p align="center">Установка</p>

1. **Клонируйте репозиторий:**
````
git clone https://github.com/ExITPerson/Coursework_3.git
````

2. **Установите зависимости:**
````
pip install -r requirements.txt
````
---

## <p align="center">Информация о тестировании проекта</p>

- **Запустите тестирование**
````
pytest --cov src --cov-report term-missing
````

- **Увидите информацию о тестах папки scr в терминале**

````
============================ test session starts ==============================
platform win32 -- Python 3.12.6, pytest-8.3.5, pluggy-1.6.0
configfile: pyproject.toml
plugins: cov-6.1.1
collected 4 items                                                                                                                                                                  

tests\test_api_class.py ....            [100%]

========================== tests coverage ======================================
_____________ coverage: platform win32, python 3.12.6-final-0 __________________

Name                 Stmts   Miss  Cover   Missing
--------------------------------------------------
src\__init__.py          0      0   100%
src\abs_classes.py      21      6    71%   9, 17, 21, 25, 29, 33
src\api_class.py        20      0   100%
src\config.py           11     11     0%   1-20
src\db_manager.py       32     32     0%   1-80
src\interaction.py      42     42     0%   1-107
src\utils.py            27     27     0%   1-104
--------------------------------------------------
TOTAL                  153    118    23%
============================ 4 passed in 0.67s ===================================
````
