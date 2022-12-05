def stop_words(words: list):
    def inner(func):
        def wrapper(*args):
            string = func(*args)

            for word in words:
                string = string.replace(word, "*")

            return string

        return wrapper

    return inner


@stop_words(["pepsi", "BMW"])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


assert create_slogan("Steve") == "Steve drinks * in his brand new *!"

