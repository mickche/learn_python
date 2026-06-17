from rich.console import Console
from rich.table import Table
from rich.theme import Theme

custom_theme = Theme({
    "text": 'green',
    "nickname": "bold yellow",
    "name": "magenta",
    "age": "blue",
    "hobbies": "cyan",
})

console = Console(theme=custom_theme)

users = {}

console.print('Привіт, я робот, який збирає дані про користувачів \nНапишіть відповіді на запитання:\n', style="italic cyan")

def get_name() -> str:
    return console.input('[text]Enter your name plz: [/]')

def get_age() -> int:
    try:
        return int(console.input("[text]Enter your age plz: [/]"))
    except ValueError:
        console.print("Це не число! вік: 0", style='bold red')
        return 0

def get_hobbies() -> list[str]:
    hobbies = []
    for h in range(3):
        hobby = console.input(f'[text]What is your {h+1} hobby: [/]')
        hobbies.append(hobby)
    return hobbies

def add_data_to_users(users: dict) -> dict:
    nickname = console.input('[text]Enter your nickname plz: [/]')

    users[nickname] = {
        'name': get_name(),
        'age': get_age(),
        'hobbies': get_hobbies()
    }
    
    return users

def print_users_table(users: dict) -> Table:
    table = Table(
        title="Users", 
        show_header=True, 
    )

    table.add_column('Nickname')
    table.add_column('Name')
    table.add_column('Age')
    table.add_column('Hobbies', justify='center')

    for nickname, info in users.items():
        hobbies_str = ", ".join(info['hobbies'])
        
        table.add_row(
            f"[nickname]{nickname}[/]",         
            f"[name]{info['name']}[/]",
            f"[age]{info['age']}[/]",
            f"[hobbies]{hobbies_str}[/]"
        )

    return table

if __name__ == '__main__':
    users = add_data_to_users(users)

    console.print("-" * 20)

    console.print(print_users_table(users))