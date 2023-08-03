import os 
from django.core.exceptions import ImproperlyConfigured


def get_secret(secret):
    """
        Returns the value of secret value from environment
    """
    try:
        value=os.environ[secret]
        return value
    except KeyError:
        msg=f"Please insert the value of {secret} in environment!!!"
        raise ImproperlyConfigured(msg)