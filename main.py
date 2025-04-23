def get_full_name(first_name: str, last_name: str):
    full_name = first_name.title() + " " + last_name.title()
    return full_name


print(get_full_name("john", "doe"))


def get_name_with_age(name: str, age: int):
    name_with_age = name + " is this old: " + str(age)
    return name_with_age


def process_items(items: list[str]):
    for item in items:
        print(item)


def process_items_tuple_set(items_t: tuple[int, int, str], items_s: set[bytes]):
    return items_t, items_s


def process_items_dict(prices: dict[str, float]):
    for item_name, item_price in prices.items():
        print(item_name)
        print(item_price)


def process_union(item: int | str):
    print(item)
    print(type(item))


def say_hi(name: str | None = None):
    if name is not None:
        print(f"Hey {name}!")
    else:
        print("Hello World")


def say_hi2(name: str | None):
    print(f"Hey {name}!")


class Person:
    def __init__(self, name: str):
        self.name = name


def get_person_name(one_person: Person):
    return one_person.name
