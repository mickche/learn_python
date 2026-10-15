## 1. Змінні та типи даних

!!! success "Правильна робота зі змінними"

    ```python
    user_age = 25
    user_name = "Олексій"

    x, y, z = 1, 2, 3
    ```

??? failure "1. Використання зарезервованого слова"

    ```python
    class = "10-B"
    # SyntaxError: invalid syntax
    ```

??? failure "2. Перезапис вбудованої функції"

    ```python
    list = [1, 2, 3]
    new_items = list("hello") 
    # TypeError: 'list' object is not callable
    ```

??? failure "3. Назва починається з цифри"

    ```python
    1st_user = "Anna"
    # SyntaxError: invalid decimal literal
    ```

??? failure "4. Використання змінної до оголошення"

    ```python
    print(total_price)
    total_price = 100
    # NameError: name 'total_price' is not defined
    ```

??? failure "5. Плутанина з регістром"

    ```python
    user_count = 10
    print(User_Count)
    # NameError: name 'User_Count' is not defined
    ```

??? failure "6. Використання дефіса в імені"

    ```python
    user-age = 20
    # SyntaxError: cannot assign to expression here
    ```

??? failure "7. Помилка розпаковки)"

    ```python
    x, y = 1, 2, 3
    # ValueError: too many values to unpack (expected 2)
    ```

??? failure "8. Додавання несумісних типів"

    ```python
    counter = "10"
    counter += 1
    # TypeError: can only concatenate str (not "int") to str
    ```

??? failure "9. Пробіли в назві"

    ```python
    first name = "John"
    # SyntaxError: invalid syntax
    ```

??? failure "10. Зміна глобальної змінної"

    ```python
    total = 0

    def add_item(price):
        total += price
    # UnboundLocalError: cannot access local variable 'total'
    ```

## 2. Рядки

!!! success

    ```python
    name = "Олена"
    age = 22
    message = f"Привіт, мене звати {name}, мені {age} років."
    ```

??? failure

    ```python
    text = "hello"
    text[0] = "H"
    # TypeError: 'str' object does not support item assignment
    ```

??? failure

    ```python
    phrase = 'It's a beautiful day'
    # SyntaxError: invalid syntax
    ```

??? failure

    ```python
    score = 100
    info = "Результат: " + score
    # TypeError: can only concatenate str (not "int") to str
    ```

??? failure

    ```python
    word = "Py"
    print(word[5])
    # IndexError: string index out of range
    ```

??? failure

    ```python
    text = "apple"
    text.replace("a", "b")
    print(text)  # Надрукує "apple"
    ```

??? failure

    ```python
    text = "python"
    if text.find("z"):
        print("Знайдено!")  # -1 оцінюється як True!
    ```

??? failure

    ```python
    name = "Іван"
    msg = "Привіт, {name}"  # Не замінить змінну
    ```

??? failure

    ```python
    text = "one two three"
    print(text[0])  # Надрукує 'o', а не 'one'
    ```

??? failure

    ```python
    words = ["a", "b", "c"]
    result = words.join("-")
    # AttributeError: 'list' object has no attribute 'join'
    ```

??? failure

    ```python
    s1 = "Admin"
    s2 = "admin"
    if s1 == s2:
        print("Одне й те саме")  # Поверне False
    ```

---

## 3. Математика та числа

!!! success

    ```python
    import math

    square = 5 ** 2
    sqrt_val = math.sqrt(25)
    ```

??? failure

    ```python
    result = 10 / 0
    # ZeroDivisionError: division by zero
    ```

??? failure

    ```python
    res = 10 / 2  # Дає float 5.0
    if res is int:
        print("Це int")  # False
    ```

??? failure

    ```python
    result = 2 ^ 3  # Це побітове XOR!
    print(result)   # Надрукує 1 замість 8
    ```

??? failure

    ```python
    print(round(2.5))  # Надрукує 2, а не 3!
    ```

??? failure 

    ```python
    if 0.1 + 0.2 == 0.3:
        print("Рівні")  # Поверне False!
    ```

??? failure

    ```python
    val = "12.5"
    number = int(val)
    # ValueError: invalid literal for int()
    ```

??? failure 

    ```python
    res = 10 + 20 / 2  # Дасть 20.0 замість (10+20)/2 = 15.0
    ```

??? failure

    ```python
    import math
    math = 10
    print(math.sqrt(16))
    # AttributeError: 'int' object has no attribute 'sqrt'
    ```

??? failure

    ```python
    import math
    val = math.sqrt(-9)
    # ValueError: math domain error
    ```

??? failure

    ```python
    count = 5
    count++
    # SyntaxError: invalid syntax
    ```

---

## 4. Списки 

!!! success

    ```python
    fruits = ["apple", "banana"]
    fruits.append("cherry")
    if "banana" in fruits:
        fruits.remove("banana")
    ```

??? failure

    ```python
    nums = [1, 2, 3]
    nums[3] = 4
    # IndexError: list assignment index out of range
    ```

??? failure

    ```python
    nums = [1, 2]
    nums.append([3, 4])  # Отримаємо [1, 2, [3, 4]]
    ```

??? failure

    ```python
    nums = [3, 1, 2]
    nums = nums.sort()
    print(nums)  # None!
    ```

??? failure

    ```python
    nums = [1, 2, 3, 4]
    for n in nums:
        if n % 2 == 0:
            nums.remove(n)  # Пропустить елементи!
    ```

??? failure

    ```python
    a = [1, 2, 3]
    b = a
    b.append(4)  # Змінить і список 'a'!
    ```

??? failure

    ```python
    empty = []
    item = empty.pop()
    # IndexError: pop from empty list
    ```

??? failure

    ```python
    colors = ["red", "green"]
    idx = colors.index("blue")
    # ValueError: 'blue' is not in list
    ```

??? failure

    ```python
    list = [1, 2]
    # Зламана функція list()
    ```

??? failure

    ```python
    items = ["a", "b", "c"]
    last = items[len(items)]
    # IndexError: list index out of range
    ```

??? failure

    ```python
    nums = [1, 2, 3]
    nums = nums + 4
    # TypeError: can only concatenate list (not "int") to list
    ```

---

## 5. Словники 

!!! success

    ```python
    user = {"name": "Ольга", "age": 28}
    city = user.get("city", "Не вказано")
    ```

??? failure

    ```python
    user = {"name": "Ivan"}
    print(user["age"])
    # KeyError: 'age'
    ```

??? failure

    ```python
    data = {[1, 2]: "numbers"}
    # TypeError: unhashable type: 'list'
    ```

??? failure

    ```python
    d = {"a": 1, "b": 2}
    for val in d:
        print(val + 10)  # val — це 'a' та 'b'
    # TypeError: can only concatenate str to str
    ```

??? failure

    ```python
    d = {"a": 1, "b": 2}
    for k in d:
        del d[k]
    # RuntimeError: dictionary changed size during iteration
    ```

??? failure

    ```python
    d = {"a": 1}
    for k, v in d:
        print(k, v)
    # TypeError: cannot unpack non-iterable str object
    ```

??? failure

    ```python
    d = dict.fromkeys(["a", "b"], [])
    d["a"].append(1)  # Спільний список у всіх ключів!
    ```

??? failure

    ```python
    def clear_data(d):
        d = {}  # Змінить лише локальне посилання!
    ```

??? failure

    ```python
    d = {"a": 1}
    d = d.update({"b": 2})
    print(d)  # None!
    ```

??? failure

    ```python
    d = {"a": 1}
    d.append({"b": 2})
    # AttributeError: 'dict' object has no attribute 'append'
    ```

??? failure

    ```python
    d = {1: "int", "1": "str"}
    # d[1] та d["1"] — це різні елементи
    ```

---

## 6. Цикли `for`

!!! success

    ```python
    fruits = ["apple", "banana", "cherry"]

    for index, fruit in enumerate(fruits, start=1):
        print(f"{index}. {fruit}")
    ```

??? failure

    ```python
    for i in range(0, 5, 0.5):
        print(i)
    # TypeError: 'float' object cannot be interpreted as an integer
    ```

??? failure

    ```python
    items = ["a", "b", "c"]
    for i in range(len(items)):
        print(items[i])
    ```

??? failure

    ```python
    for i in range(5):
        i += 2  # Не вплине на наступну ітерацію!
    ```

??? failure

    ```python
    for i in 5:
        print(i)
    # TypeError: 'int' object is not iterable
    ```

??? failure

    ```python
    import itertools
    for i in itertools.count(1):
        pass  # Зациклиться без break!
    ```

??? failure

    ```python
    for i in range(3):
        if i == 1:
            break
    else:
        print("Готово")  # Не виконається через break!
    ```

??? failure

    ```python
    for item in []:
        pass
    print(item)
    # NameError: name 'item' is not defined
    ```

??? failure

    ```python
    def check_evens(numbers):
        for n in numbers:
            if n % 2 == 0: return True
            else: return False  # Перерве цикл одразу!
    ```

??? failure

    ```python
    names = ["Anna", "Max"]
    ages = [20, 25]
    for name, age in names, ages:
        pass
    ```

??? failure 

    ```python
    numbers = [1, 2, 3, 4]
    for num in numbers:
        numbers.remove(num)
    ```

---

## 7. Функції

!!! success "Правильне визначення та використання функцій"

    ```python
    def greet_user(name: str, role: str = "guest") -> str:
        return f"Привіт, {name}! Твій статус: {role}."

    message = greet_user("Олексій", role="admin")
    ```

??? failure

    ```python
    def add_item(item, items=[]):
        items.append(item)
        return items
    # Завжди повертає один і той самий список!
    ```

??? failure

    ```python
    def sum_vals(a, b):
        res = a + b

    total = sum_vals(5, 5)  # total дорівнює None!
    ```

??? failure

    ```python
    def create(name, age): pass
    create(name="Alex", 20)
    # SyntaxError: positional argument follows keyword argument
    ```

??? failure

    ```python
    count = 0
    def inc():
        count += 1
    # UnboundLocalError
    ```

??? failure

    ```python
    def mul(a, b): return a * b
    mul(5)
    # TypeError: missing 1 required positional argument
    ```

??? failure

    ```python
    def square(x): print(x**2)
    res = square(4)  # res = None
    ```

??? failure

    ```python
    def func(**kwargs, *args): pass
    # SyntaxError: invalid syntax
    ```

??? failure

    ```python
    run()
    def run(): pass
    # NameError: name 'run' is not defined
    ```

??? failure

    ```python
    def get_pt(): return 1, 2, 3
    x, y = get_pt()
    # ValueError: too many values to unpack
    ```

??? failure

    ```python
    def parse(list):
        return list(set(list))
    # TypeError: 'list' object is not callable
    ```