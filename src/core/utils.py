from django.contrib.auth.hashers import BasePasswordHasher

class NoSaltPasswordHasher(BasePasswordHasher):
    """
        Django by default make every password salted this way even two
        users with same password won't have the same hashed password 
        This code disables it (you should add it to settings.py)
        Intentional vulnerability (DO NOT USE IN REAL WORLD CODE).
    """
    algorithm = "nosalt"

    def encode(self, password, salt):
        return password

    def verify(self, password, encoded):
        return password == encoded

    def safe_summary(self, encoded):
        return {"algorithm": self.algorithm, "iterations": 1}