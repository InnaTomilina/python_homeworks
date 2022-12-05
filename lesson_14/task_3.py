def arg_rules(type_: type, max_length: int, contains: list):
    def has_contains_in(name):
        for word in contains:
            if word not in name:
                return False

        return True

    def inner(func):
        def wrapper(name):
            if (
                isinstance(name, type_)
                and len(name) <= max_length
                and has_contains_in(name)
            ):
                return func(name)

            return False

        return wrapper

    return inner


@arg_rules(type_=str, max_length=15, contains=["05", "@"])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


assert create_slogan("johndoe05@gmail.com") is False
assert create_slogan("S@SH05") == "S@SH05 drinks pepsi in his brand new BMW!"