# Словники

## Словники - це не впорядкована структура даних яка має унікальні ключі та зачення(можуть бути будь-якого типу)

Приклад:

``` python

my_dict = {
    'name': 'Cateika',
    'age': 5,
    'color': "orange"
}

```


??? tip

    Щоб створити порожній словник можна за допомогую `{}` або `dict()`


###  Додавання елементів до словника

В *списках* це було через `.append()` а от в словниках це так:

``` python  

my_dict['type'] = 'cat' 

print()
#  {'name': 'Cateika', 'age': 5 'color': "orange", type: 'cat'}

```



### Оновлення словників

`.update` може додавати нові пари та змінювати які вже є:

``` python

my_dict.update('name':'Barsik')
print(my_dict)
#  {'name': 'Barsik', 'age': 5 'color': "orange", type: 'cat'}


```

### Видалення елементів зі словника

``` python

#1

del my_dict['name']

print(my_dict)
# { 'age': 5 'color': "orange", type: 'cat'}

#2
my_dict.pop('name')
print(my_dict)
# { 'age': 5 'color': "orange", type: 'cat'}

```


# ==FILE IN DEVELOPMENT==