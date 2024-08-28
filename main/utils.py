import random
from django.core.mail import send_mail
from django.conf import settings

def genereate_auth_code():
    characters = '0123456789'
    auth_code = ''.join(random.choice(characters) for i in range(6))
    return auth_code


def send_verification_email(user):
    auth_code = genereate_auth_code()
    subject = "Ro'yxatdan o'tish muvaffaqiyatli yakunlandi !"
    msg = f"Email manzilni tasdiqlash kodi: {auth_code}"
    from_email = settings.EMAIL_HOST_USER
    to_email = [user.email]
    user.auth_code = auth_code
    user.save()
    send_mail(subject, msg, from_email, to_email, fail_silently=False)

