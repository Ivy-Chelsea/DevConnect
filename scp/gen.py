import random
from string import ascii_letters


def generate_room_code(length: int, existing_code):
    while True:
        code_chars = [random.choice(ascii_letters) for _ in range(length)]
        code = ''.join(code_chars)
        if code not in existing_code:
            return code
