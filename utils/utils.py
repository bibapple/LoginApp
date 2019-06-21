import hashlib
import datetime
from login.models import ConfirmEmail


def hash_code(original, salt="LoginApp"):
    h = hashlib.sha256()
    original += salt
    h.update(original.encode())
    return h.hexdigest()


def make_confirm_email(user):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    code = hash_code(user.name, now)
    ConfirmEmail.objects.create(code=code, user=user)
    return code

