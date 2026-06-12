# json_vs_jsonl


## Чим JSONL краще за JSON?


### По перше, його економія оперативної пам'яті
Коли ви щось робите з файлом то пи по стрічці перевіряєте, замість всього файлу
Це буде видно якщо в вас буде ==JSON на 10000000+ стрічок "(Такі є)"==

### По друге, це стійкість до помилок
Якщо в **JSON** буде хоч одна помилка, все зламається
А у **JSONL** ви можете просто дописувати нові рядки в кінець файлу. Якщо програма вилетить, ви втратите лише той один рядок, який записувався в цей момент. Інші дані не постраждають.



# Порівняння коду 


=== "json"
    ```json linenums="1"
        [
        {"id": 1, "name": "Олексій", "role": "admin"},
        {"id": 2, "name": "Кірілл", "role": "user_devops"},
        {"id": 3, "name": "Іра", "role": "best_user"}
        ]
    ```
    
=== "jsonl"
    ```jsonl linenums="1"
    {"id": 1, "name": "Олексій", "role": "admin"}
    {"id": 2, "name": "Кірілл", "role": "user_devops"}
    {"id": 3, "name": "Іра", "role": "best_user"}
    ```


## Читання 

=== "json"
    ```py linenums="1"
    import json

    with open("data.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    for item in data:
        print(item["name"])
    ```
    
=== "jsonl"
    ```py linenums="1"
    import json

    with open("data.jsonl", "r", encoding="utf-8") as f:
        for line in f:
            item = json.loads(line.strip())
            print(item["name"])
    ```

Як я вже казав раніше, якщо ==JSON== буде великим, то він буде навантажувати ==оперативну пам'ять==

А ==JSONL== навантажує менше, бо він ==перевіряє по стрічці==

## Додавання

=== "json"
    ```py linenums="1"
    import json
    data = [
        {"name": "Alice", "age": 25},
        {"name": "Bob", "age": 30}
        ]

    with open('data.json', 'w') as f:
        json.dump(data, f,)
    ```
    
=== "jsonl"
    ```py linenums="1"
    import json

    data = [
        {"name": "Alice", "age": 25},
        {"name": "Bob", "age": 30}
        ]

    with open('data.jsonl', 'w') as f:
        for item in data:
            f.write(json.dumps(item))
    ```

Якщо порівнювати то ==JSONL краще==, якщо буде якась помилка в написані коду то все що зберіглося раніше, буде в файлі
