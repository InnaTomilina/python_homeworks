class CustomException(Exception):
    def __init__(self, msg):
        file = open("logs.txt", "a")
        file.write(msg)
        file.close()

        super().__init__(msg)

raise CustomException ("hello world!")