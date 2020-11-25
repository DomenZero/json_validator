# Анализ JSON скриптов по схемам
#### Быстрый запуск 
В папке dist лежит exe-файл json_validate.exe
Для запуска необходимо в консоли ввести 
>  json_validate.exe --fscript "event" --fschema "./schema/"

--fscript - указывает на папку со скриптами
--fschema - указывает на папку со схемами
В результате будет html и log файлы

#### Установка библиотеки
Для JSON анализа
> pip install 

Для вывода в html
> pip install dominate

#### Запуск скрипта
Пример:  
./event - папка со скриптами JSON  
./schema - папка со схемами JSON

> python main.py --fscript "./event" --fschema "./schema/"  

#### Результаты выполнения скрипта
Файлы:  
index.html - таблица где есть столбцы: 
* первый - путь к JSON скрипту
* второй - путь к JSON схеме
* третий - код ошибки  

app.log - содержит лог выполнения скрипта,  выводит содержимое проверяемых файлов 
```html
<!DOCTYPE html>
<html>
  <head>
    <title>JSON validator</title>
    <link href="style.css" rel="stylesheet">
    <script src="script.js" type="text/javascript"></script>
  </head>
  <body>
    <div class="container">
      <table class="table table-striped" id="main">
        <caption>
          <h3>JSON valid</h3>
        </caption>
        <thead>
          <tr>
            <th>JSON script</th>
            <th>JSON schema</th>
            <th>Error</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>./event\1eba2aa1-2acf-460d-91e6-55a8c3e3b7a3.json</td>
            <td>./schema/cmarker_created.schema</td>
            <td>'cmarkers' is a required property</td>
          </tr>
          <tr>
            <td>./event\1eba2aa1-2acf-460d-91e6-55a8c3e3b7a3.json</td>
            <td>./schema/label_selected.schema</td>
            <td>'id' is a required property</td>
          </tr>
          <tr>
            <td>./event\1eba2aa1-2acf-460d-91e6-55a8c3e3b7a3.json</td>
            <td>./schema/sleep_created.schema</td>
            <td>'source' is a required property</td>
          </tr>
          <tr>
            <td>./event\1eba2aa1-2acf-460d-91e6-55a8c3e3b7a3.json</td>
            <td>./schema/workout_created.schema</td>
            <td>'activity_name' is a required property</td>
          </tr>
          <tr>
            <td>./event\297e4dc6-07d1-420d-a5ae-e4aff3aedc19.json</td>
            <td>./schema/cmarker_created.schema</td>
            <td>'cmarkers' is a required property</td>
          </tr>
          <tr>
            <td>./event\297e4dc6-07d1-420d-a5ae-e4aff3aedc19.json</td>
            <td>./schema/label_selected.schema</td>
            <td>'labels' is a required property</td>
          </tr>
          <tr>
            <td>./event\297e4dc6-07d1-420d-a5ae-e4aff3aedc19.json</td>
            <td>./schema/sleep_created.schema</td>
            <td>'source' is a required property</td>
          </tr>
          <tr>
            <td>./event\297e4dc6-07d1-420d-a5ae-e4aff3aedc19.json</td>
            <td>./schema/workout_created.schema</td>
            <td>'activity_name' is a required property</td>
          </tr>
          <tr>
            <td>./event\29f0bfa7-bd51-4d45-93be-f6ead1ae0b96.json</td>
            <td>./schema/cmarker_created.schema</td>
            <td>None is not of type 'object'</td>
          </tr>
          <tr>
            <td>./event\29f0bfa7-bd51-4d45-93be-f6ead1ae0b96.json</td>
            <td>./schema/label_selected.schema</td>
            <td>None is not of type 'object'</td>
          </tr>
          <tr>
            <td>./event\29f0bfa7-bd51-4d45-93be-f6ead1ae0b96.json</td>
            <td>./schema/sleep_created.schema</td>
            <td>None is not of type 'object'</td>
          </tr>
          <tr>
            <td>./event\29f0bfa7-bd51-4d45-93be-f6ead1ae0b96.json</td>
            <td>./schema/workout_created.schema</td>
            <td>None is not of type 'object'</td>
          </tr>
          <tr>
            <td>./event\2e8ffd3c-dbda-42df-9901-b7a30869511a.json</td>
            <td>./schema/cmarker_created.schema</td>
            <td>'cmarkers' is a required property</td>
          </tr>
          <tr>
            <td>./event\2e8ffd3c-dbda-42df-9901-b7a30869511a.json</td>
            <td>./schema/label_selected.schema</td>
            <td>'labels' is a required property</td>
          </tr>
          <tr>
            <td>./event\2e8ffd3c-dbda-42df-9901-b7a30869511a.json</td>
            <td>./schema/sleep_created.schema</td>
            <td>'source' is a required property</td>
          </tr>
          <tr>
            <td>./event\2e8ffd3c-dbda-42df-9901-b7a30869511a.json</td>
            <td>./schema/workout_created.schema</td>
            <td>'activity_name' is a required property</td>
          </tr>
          <tr>
            <td>./event\3ade063d-d1b9-453f-85b4-dda7bfda4711.json</td>
            <td>./schema/cmarker_created.schema</td>
            <td>'cmarkers' is a required property</td>
          </tr>
          <tr>
            <td>./event\3ade063d-d1b9-453f-85b4-dda7bfda4711.json</td>
            <td>./schema/label_selected.schema</td>
            <td>'labels' is a required property</td>
          </tr>
          <tr>
            <td>./event\3ade063d-d1b9-453f-85b4-dda7bfda4711.json</td>
            <td>./schema/sleep_created.schema</td>
            <td>'source' is a required property</td>
          </tr>
          <tr>
            <td>./event\3ade063d-d1b9-453f-85b4-dda7bfda4711.json</td>
            <td>./schema/workout_created.schema</td>
            <td>'activity_name' is a required property</td>
          </tr>
          <tr>
            <td>./event\3b4088ef-7521-4114-ac56-57c68632d431.json</td>
            <td>./schema/cmarker_created.schema</td>
            <td>'cmarkers' is a required property</td>
          </tr>
          <tr>
            <td>./event\3b4088ef-7521-4114-ac56-57c68632d431.json</td>
            <td>./schema/label_selected.schema</td>
            <td>'labels' is a required property</td>
          </tr>
          <tr>
            <td>./event\3b4088ef-7521-4114-ac56-57c68632d431.json</td>
            <td>./schema/sleep_created.schema</td>
            <td>'source' is a required property</td>
          </tr>
          <tr>
            <td>./event\3b4088ef-7521-4114-ac56-57c68632d431.json</td>
            <td>./schema/workout_created.schema</td>
            <td>'activity_name' is a required property</td>
          </tr>
          <tr>
            <td>./event\6b1984e5-4092-4279-9dce-bdaa831c7932.json</td>
            <td>./schema/cmarker_created.schema</td>
            <td>'cmarkers' is a required property</td>
          </tr>
          <tr>
            <td>./event\6b1984e5-4092-4279-9dce-bdaa831c7932.json</td>
            <td>./schema/label_selected.schema</td>
            <td>'labels' is a required property</td>
          </tr>
          <tr>
            <td>./event\6b1984e5-4092-4279-9dce-bdaa831c7932.json</td>
            <td>./schema/sleep_created.schema</td>
            <td>'source' is a required property</td>
          </tr>
          <tr>
            <td>./event\6b1984e5-4092-4279-9dce-bdaa831c7932.json</td>
            <td>./schema/workout_created.schema</td>
            <td>'activity_name' is a required property</td>
          </tr>
          <tr>
            <td>./event\a95d845c-8d9e-4e07-8948-275167643a40.json</td>
            <td>./schema/cmarker_created.schema</td>
            <td>'cmarkers' is a required property</td>
          </tr>
          <tr>
            <td>./event\a95d845c-8d9e-4e07-8948-275167643a40.json</td>
            <td>./schema/label_selected.schema</td>
            <td>'id' is a required property</td>
          </tr>
          <tr>
            <td>./event\a95d845c-8d9e-4e07-8948-275167643a40.json</td>
            <td>./schema/sleep_created.schema</td>
            <td>'source' is a required property</td>
          </tr>
          <tr>
            <td>./event\a95d845c-8d9e-4e07-8948-275167643a40.json</td>
            <td>./schema/workout_created.schema</td>
            <td>'activity_name' is a required property</td>
          </tr>
          <tr>
            <td>./event\ba25151c-914f-4f47-909a-7a65a6339f34.json</td>
            <td>./schema/cmarker_created.schema</td>
            <td>'cmarkers' is a required property</td>
          </tr>
          <tr>
            <td>./event\ba25151c-914f-4f47-909a-7a65a6339f34.json</td>
            <td>./schema/label_selected.schema</td>
            <td>'id' is a required property</td>
          </tr>
          <tr>
            <td>./event\ba25151c-914f-4f47-909a-7a65a6339f34.json</td>
            <td>./schema/sleep_created.schema</td>
            <td>'source' is a required property</td>
          </tr>
          <tr>
            <td>./event\ba25151c-914f-4f47-909a-7a65a6339f34.json</td>
            <td>./schema/workout_created.schema</td>
            <td>'activity_name' is a required property</td>
          </tr>
          <tr>
            <td>./event\bb998113-bc02-4cd1-9410-d9ae94f53eb0.json</td>
            <td>./schema/cmarker_created.schema</td>
            <td>'cmarkers' is a required property</td>
          </tr>
          <tr>
            <td>./event\bb998113-bc02-4cd1-9410-d9ae94f53eb0.json</td>
            <td>./schema/label_selected.schema</td>
            <td>'labels' is a required property</td>
          </tr>
          <tr>
            <td>./event\bb998113-bc02-4cd1-9410-d9ae94f53eb0.json</td>
            <td>./schema/sleep_created.schema</td>
            <td>'source' is a required property</td>
          </tr>
          <tr>
            <td>./event\bb998113-bc02-4cd1-9410-d9ae94f53eb0.json</td>
            <td>./schema/workout_created.schema</td>
            <td>'activity_name' is a required property</td>
          </tr>
          <tr>
            <td>./event\c72d21cf-1152-4d8e-b649-e198149d5bbb.json</td>
            <td>./schema/cmarker_created.schema</td>
            <td>'cmarkers' is a required property</td>
          </tr>
          <tr>
            <td>./event\c72d21cf-1152-4d8e-b649-e198149d5bbb.json</td>
            <td>./schema/label_selected.schema</td>
            <td>'labels' is a required property</td>
          </tr>
          <tr>
            <td>./event\c72d21cf-1152-4d8e-b649-e198149d5bbb.json</td>
            <td>./schema/sleep_created.schema</td>
            <td>'source' is a required property</td>
          </tr>
          <tr>
            <td>./event\c72d21cf-1152-4d8e-b649-e198149d5bbb.json</td>
            <td>./schema/workout_created.schema</td>
            <td>'activity_name' is a required property</td>
          </tr>
          <tr>
            <td>./event\cc07e442-7986-4714-8fc2-ac2256690a90.json</td>
            <td>./schema/cmarker_created.schema</td>
            <td>'cmarkers' is a required property</td>
          </tr>
          <tr>
            <td>./event\cc07e442-7986-4714-8fc2-ac2256690a90.json</td>
            <td>./schema/label_selected.schema</td>
            <td>'id' is a required property</td>
          </tr>
          <tr>
            <td>./event\cc07e442-7986-4714-8fc2-ac2256690a90.json</td>
            <td>./schema/sleep_created.schema</td>
            <td>'source' is a required property</td>
          </tr>
          <tr>
            <td>./event\cc07e442-7986-4714-8fc2-ac2256690a90.json</td>
            <td>./schema/workout_created.schema</td>
            <td>'activity_name' is a required property</td>
          </tr>
          <tr>
            <td>./event\e2d760c3-7e10-4464-ab22-7fda6b5e2562.json</td>
            <td>./schema/cmarker_created.schema</td>
            <td>'cmarkers' is a required property</td>
          </tr>
          <tr>
            <td>./event\e2d760c3-7e10-4464-ab22-7fda6b5e2562.json</td>
            <td>./schema/label_selected.schema</td>
            <td>'labels' is a required property</td>
          </tr>
          <tr>
            <td>./event\e2d760c3-7e10-4464-ab22-7fda6b5e2562.json</td>
            <td>./schema/sleep_created.schema</td>
            <td>'source' is a required property</td>
          </tr>
          <tr>
            <td>./event\e2d760c3-7e10-4464-ab22-7fda6b5e2562.json</td>
            <td>./schema/workout_created.schema</td>
            <td>'activity_name' is a required property</td>
          </tr>
          <tr>
            <td>./event\f5656ff6-29e1-46b0-8d8a-ff77f9cc0953.json</td>
            <td>./schema/cmarker_created.schema</td>
            <td>'cmarkers' is a required property</td>
          </tr>
          <tr>
            <td>./event\f5656ff6-29e1-46b0-8d8a-ff77f9cc0953.json</td>
            <td>./schema/label_selected.schema</td>
            <td>'labels' is a required property</td>
          </tr>
          <tr>
            <td>./event\f5656ff6-29e1-46b0-8d8a-ff77f9cc0953.json</td>
            <td>./schema/sleep_created.schema</td>
            <td>'source' is a required property</td>
          </tr>
          <tr>
            <td>./event\f5656ff6-29e1-46b0-8d8a-ff77f9cc0953.json</td>
            <td>./schema/workout_created.schema</td>
            <td>'activity_name' is a required property</td>
          </tr>
          <tr>
            <td>./event\fb1a0854-9535-404d-9bdd-9ec0abb6cd6c.json</td>
            <td>./schema/cmarker_created.schema</td>
            <td>'cmarkers' is a required property</td>
          </tr>
          <tr>
            <td>./event\fb1a0854-9535-404d-9bdd-9ec0abb6cd6c.json</td>
            <td>./schema/label_selected.schema</td>
            <td>'labels' is a required property</td>
          </tr>
          <tr>
            <td>./event\fb1a0854-9535-404d-9bdd-9ec0abb6cd6c.json</td>
            <td>./schema/sleep_created.schema</td>
            <td>'source' is a required property</td>
          </tr>
          <tr>
            <td>./event\fb1a0854-9535-404d-9bdd-9ec0abb6cd6c.json</td>
            <td>./schema/workout_created.schema</td>
            <td>'activity_name' is a required property</td>
          </tr>
          <tr>
            <td>./event\ffe6b214-d543-40a8-8da3-deb0dc5bbd8c.json</td>
            <td>./schema/cmarker_created.schema</td>
            <td>'cmarkers' is a required property</td>
          </tr>
          <tr>
            <td>./event\ffe6b214-d543-40a8-8da3-deb0dc5bbd8c.json</td>
            <td>./schema/label_selected.schema</td>
            <td>'labels' is a required property</td>
          </tr>
          <tr>
            <td>./event\ffe6b214-d543-40a8-8da3-deb0dc5bbd8c.json</td>
            <td>./schema/sleep_created.schema</td>
            <td>'source' is a required property</td>
          </tr>
          <tr>
            <td>./event\ffe6b214-d543-40a8-8da3-deb0dc5bbd8c.json</td>
            <td>./schema/workout_created.schema</td>
            <td>'activity_name' is a required property</td>
          </tr>
        </tbody>
      </table>
    </div>
  </body>
</html>
```