class User:

    def __init__(self, name="", email=""):
        self.name, self.email = name, email

    @classmethod
    def all(cls):
        return {
        'Thor': ["thor@heimdall.com", 1500],
        'Loki': ["loki@heimdall.com", 1000],
        'Valkyrie': ["valkyrie@heimdall.com", 5000],
        }

    def verify(self) -> bool:
        print(self.name, self.email)
        name = self.name in User.all()
        email = any(1 for user_info in User.all().values() if self.email == user_info[0])
        return {"results": name and email}
