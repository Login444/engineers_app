﻿# engineers_app
Сервис реализован с использованием фреймворка FastAPI.

**Сущности(entity)**
Реализована модель Team с полями:
1. id - индентификатор команды
2. name - название команды
3. members - список (list) участников команды

**Хранение в памяти**
На данном этапе, что бы не заполнять большие ресурсы в памяти, было принято решение создать внутренний класс TeamRepository.
В этот класс сохраняется словарь (dict) существующих команд инженеров, где ключ - id команды, значение - сама сущность команды (id, name, members).
Так же были реализованы основные методы по работе с командами в памяти программы: Create, Update, Delete, Get.
При необходимости можно создать БД на основе уже описанных связей.

**Usecase**
Отдельно был реализован юзкейс для работы с репозиторием и командами.
Так же были реализованы все основные функции CRUD.

**main**
Было осуществленно подключение всех прописанных функций к экземпляру класса FastAPI, реализованы методы POST, PUT, DELETE, GET.
