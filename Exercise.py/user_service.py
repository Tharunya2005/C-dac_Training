__users = []

def user_count() -> int:
    return len(__users)


def add_user(username: str) -> None:
    global __users
    __users += [username]


def delete_user_by_index(index: int) -> str:
    global __users
    if index >=0 or index < len(__users):
        return __users.pop(index)
    
    raise IndexError(f"Invalid index. Must be between 0 and {len(__users)-1}")

def delete_user_by_name(username: str) -> str:
    ...


def print_users() -> None:
    global __users
    for index, each_user in enumerate(__users):
        print(f'{index} - {each_user}')