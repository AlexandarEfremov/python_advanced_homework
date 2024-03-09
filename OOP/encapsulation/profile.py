class Profile:
    def __init__(self, username: str, password: str):
        self.__username = username
        self.__password = password

        if 5 <= len(self.__username) <= 15:
            pass
        raise ValueError("The username must be between 5 and 15 characters.")

        if len(self.__password) >= 8:
            pass
        raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")
