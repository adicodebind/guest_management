import random


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
