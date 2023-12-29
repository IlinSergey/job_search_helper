from datetime import datetime

import pytest
from telegram import Chat, Message, User


@pytest.fixture
def effective_user():
    return User(
        id=123,
        first_name='Bob',
        is_bot=False,
        last_name='Squarepants',
        username='Sponge_Bob',
    )


def make_message(text, user):
    message = Message(
        message_id=1,
        date=datetime.now(),
        chat=Chat(id=1, type='PRIVAT'),
        from_user=user,
        text=text,
    )
    return message
