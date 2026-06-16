from rich.console import Console
from rich.table import Table



users = {}


def get_name() -> str:
	return input('Enter your name plz: ')

def get_age() -> int:
	return int(input('Enter your age plz: '))

def get_hobbies() -> list[str]:
	hobbies = []
	for h in range(3):
		hobbies.append(input('What is your f hobby: '))
	return hobbies

def add_data_to_users(users: dict) -> dict:
    nickname = input('Enter your nickname plz: ')

    users[nickname] = {
        'name': get_name(),
        'age': get_age(),
        'hobbies': get_hobbies()}
    
    return users


console = Console()

def print_users_table(users: dict):
    table = Table(title="Users", show_header=True, header_style="bold magenta")

    table.add_column('Nickname')
    table.add_column('Name')
    table.add_column('Age')
    table.add_column('Hobbies')

    for nickname, info in users.items():
        hobbies_str = ", ".join(info['hobbies'])
        
        table.add_row(
            nickname,        
            info['name'],
            str(info['age']),
            hobbies_str
        )

    return table

users = add_data_to_users(users)
print("-" * 20)


console.print(print_users_table(users))