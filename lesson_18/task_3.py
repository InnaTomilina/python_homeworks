class TypeDecorators:
    @classmethod
    def to_int(cls, func):
        def inner(value):
            result = func(value)

            return result if not result.isdigit() else int(result)

        return inner

    @classmethod
    def to_str(cls, func):
        def inner(value):
            str(func(value))

        return inner

    @classmethod
    def to_float(cls, func):
        def inner(value):
            result = func(value)
            is_float = result.replace(".", "", 1).isdigit()

            return result if not is_float else float(result)

        return inner

    @classmethod
    def to_bool(cls, func):
        def inner(value):
            result = func(value)

            if result in ["True", "true"]:
                return True

            if result in ["False", "false"]:
                return False

            if result.isdigit():
                return result != 0

        return inner


@TypeDecorators.to_int
def do_nothing(string: str):
    return string


@TypeDecorators.to_float
def do_not_nothing(string: str):
    return string


@TypeDecorators.to_bool
def do_something(string: str):
    return string


assert do_nothing("25") == 25
assert do_nothing("foo") == "foo"
assert do_not_nothing("23.45") == 23.45
assert do_something("True") is True
assert do_something("false") is False
