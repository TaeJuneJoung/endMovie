import os, json
import smtplib
import string
import random
from email.mime.text import MIMEText

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_DIR = os.path.join(BASE_DIR, 'secret_data')

def auth_email_check(user_email):
    with open(os.path.join(SECRET_DIR, 'secret_key.json')) as f:
        data = f.read()
    secret_key = json.loads(data)
    EMAIL_HOST_USER = secret_key.get('EMAIL_HOST_USER')
    EMAIL_HOST_PASSWORD = secret_key.get('EMAIL_HOST_PASSWORD')
    # 인증번호
    _LENGTH = 8
    string_pool = string.ascii_letters + string.digits
    
    auth_nums = ""
    for i in range(_LENGTH):
        auth_nums += random.choice(string_pool)

    smtp = smtplib.SMTP('smtp.gmail.com', 587)
    smtp.starttls()
    smtp.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
    msg = MIMEText(f'가입인증 코드입니다. \n 인증번호 : {auth_nums}')
    msg['Subject'] = 'EndMovie 가입인증 코드입니다.'

    smtp.sendmail(EMAIL_HOST_USER, user_email, msg.as_string())
    smtp.quit()
    return auth_nums