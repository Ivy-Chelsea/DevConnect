def generate_room_code(length: int, existing_code):
    while True:
        code_chars = [random.choice(ascii_letters) for _ in range(length)]

