import random
import threading

from django.core.mail import send_mail

from base.models import EmailLog


def run_in_background(func):
    def decorator(*args, **kwargs):
        t = threading.Thread(target=func, args=args, kwargs=kwargs)
        t.daemon = True
        t.start()

    return decorator


def generate_random_string(length=10, num_only=False):
    choices = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    if num_only:
        choices = "0123456789"
    selected_arr = [random.choice(choices) for _ in range(length)]

    rand_string = "".join(selected_arr)

    return rand_string


def generate_public_id(object, length=10):
    rand_string = generate_random_string(length)

    while object.__class__.objects.filter(public_id=rand_string).exists():
        rand_string = generate_random_string()

    return rand_string


def send_email_wrapper(sender, receivers, subject, message):
    send_mail(subject=subject,
              message=message,
              from_email=sender,
              recipient_list=tuple(receivers),
              fail_silently=False
              )
    EmailLog.objects.create(sender=sender, targets=",".join(receivers), subject=subject, content=message)
