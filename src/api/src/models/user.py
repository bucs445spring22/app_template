from src.db.model import Model

class User(Model):
    def model_attr(self) -> None:
        """
        [set object attributes]
        """
        self.name = ""
        self.email = ""

    def verify(self) -> bool:
        return True
