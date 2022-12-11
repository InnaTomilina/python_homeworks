class User:
    def __init__(self, email: str):
        if not User.validate(email):
            raise Exception("It is not an email address")

        self.email = email

    @classmethod
    def validate(cls, email: str):
        return isinstance(email, str) and "@" in email


user = User("foo@mail.com")
assert user.email == "foo@mail.com"

try:
    User("")
except Exception as e:
    print(e)