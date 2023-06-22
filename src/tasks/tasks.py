from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

from src.celery import celery


@celery.task()
def send_message(payload: str, to: str):
    async def send(payload, to):
        msg = MIMEMultipart()
        msg['From'] = 'pratayeu@yandex.ru'
        msg['To'] = to
        msg['Subject'] = 'FastApi'

        msg.attach(MIMEText(payload))

        server = smtplib.SMTP('smtp.yandex.ru', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()

        server.login('pratayeu@yandex.ru', 'oyyaehwnlvdwlexy')
        server.sendmail(
            'pratayeu@yandex.ru',
            to,
            msg.as_string()
        )
        server.quit()
    import asyncio
    asyncio.run(send(payload, to))


@celery.task()
def spam_machine(payload, to):
    msg = MIMEMultipart()
    msg['From'] = 'pratayeu@yandex.ru'
    msg['To'] = to
    msg['Subject'] = 'FastApi'

    msg.attach(MIMEText(payload))

    server = smtplib.SMTP('smtp.yandex.ru', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('pratayeu@yandex.ru', 'oyyaehwnlvdwlexy')
    server.sendmail(
        'pratayeu@yandex.ru',
        to,
        msg.as_string()
    )
    server.quit()
