import copy

def create_shallow_copy(data: list) -> list:
    """Returns a shallow copy of the given list."""
    return data.copy()

def create_deep_copy(data: list) -> list:
    """Returns a deep copy of the given list using copy module."""
    return copy.deepcopy(data)

def append_to_nested_list(data: list, value) -> None:
    """Appends a value to the first nested list found inside the list."""
    for item in data:
        if isinstance(item, list):
            item.append(value)
            break
