import random
from string import ascii_letters
from scp import mail



def generate_room_code(length: int, existing_code):
    while True:
        code_chars = [random.choice(ascii_letters) for _ in range(length)]
        code = ''.join(code_chars)
        if code not in existing_code:
            return code


def reset_email(user):
    token = user.get_reset_token()
    msg = Message('Password Reset Request',
                  sender='sscarlette84@gmail.com',
                  recipients=[user.email])
    msg.body = f'''To reset your password, visit the following link:
{url_for('reset_token', token=token, _external=True)}

If you did not make this request then simply ignore this email and no changes will be made.
'''
    mail.send(msg)
