import hashlib
import random
import string


ROLE_CHOICES = (
    ("customer", "Customer"),
    ("influencer", "Influencer"),
    ("admin", "Admin")
)

def generate_unique_key(value, length=40):
    """
    generate key from passed value
    :param value:
    :param length: key length
    :return:
    """

    salt = "".join(
        random.SystemRandom().choice(string.ascii_uppercase + string.digits)
        for _ in range(26)
    ).encode("utf-8")
    value = value.encode("utf-8")
    activation_key = hashlib.sha1(salt + value).hexdigest()

    return activation_key[:length]