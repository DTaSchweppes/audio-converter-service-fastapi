# audio-converter-service-fastapi
Данное приложение выполнено согласно ТЗ:  
1.Создание пользователя, POST:  
Принимает на вход запросы с именем пользователя;  
Создаёт в базе данных пользователя заданным именем, так же генерирует уникальный идентификатор пользователя и UUID токен доступа (в виде строки) для данного пользователя;  
Возвращает сгенерированные идентификатор пользователя и токен.  
2.Добавление аудиозаписи, POST:  
Принимает на вход запросы, содержащие уникальный идентификатор пользователя, токен доступа и аудиозапись в формате wav;  
Преобразует аудиозапись в формат mp3, генерирует для неё уникальный UUID идентификатор и сохраняет их в базе данных;  
Возвращает URL для скачивания записи вида http://host:port/record?id=id_записи&user=id_пользователя.  
3.Доступ к аудиозаписи, GET:  
Предоставляет возможность скачать аудиозапись по ссылке из п 2.2.3.

![image](https://github.com/DTaSchweppes/audio-converter-service-fastapi/assets/45369246/00285e90-7f40-4515-8a8a-65aaa1bd63f8)
  ![image](https://github.com/DTaSchweppes/audio-converter-service-fastapi/assets/45369246/6d8191d1-c71e-4dd6-a15a-6c8861bb673d)
результатом запроса будет строка в БД:
![image](https://github.com/DTaSchweppes/audio-converter-service-fastapi/assets/45369246/200dd130-3b26-4c2b-84fa-3652207b9ce2)
и ответ:
![image](https://github.com/DTaSchweppes/audio-converter-service-fastapi/assets/45369246/ea3e39a3-4cec-4367-917d-23325a95f849)
(Возвращает сгенерированные идентификатор пользователя и токен)
-Добавление аудиозаписи, POST:
Принимает на вход запросы, содержащие уникальный идентификатор пользователя, токен доступа и аудиозапись в формате wav:
![image](https://github.com/DTaSchweppes/audio-converter-service-fastapi/assets/45369246/85f72cae-8207-472c-90d2-5e4d7e53ba78)
Преобразует аудиозапись в формат mp3, генерирует для неё уникальный UUID идентификатор и сохраняет их в базе данных:
![image](https://github.com/DTaSchweppes/audio-converter-service-fastapi/assets/45369246/17f11554-4065-431f-832c-b6f83938f692)
Возвращает URL для скачивания записи вида http://host:port/record?id=id_записи&user=id_пользователя.
Так выглядит в БД:
![image](https://github.com/DTaSchweppes/audio-converter-service-fastapi/assets/45369246/eab52e35-b7d9-4856-afac-7a3c199e3ca8)
А на данном скриншоте представлен запрос get на загрузку аудио
![image](https://github.com/DTaSchweppes/audio-converter-service-fastapi/assets/45369246/e70513fa-3ac5-469a-a1d9-f5d631e96d14)

