from fastapi import FastAPI

from src.tasks import send_message


app = FastAPI()


@app.get('/')
async def index():
    send_message.delay('some text', 'thommy.python.dev@gmail.com')
    return {'status': 'OK'}
