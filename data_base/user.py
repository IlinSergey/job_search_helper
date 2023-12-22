from db import db_session
from models import User
from telegram import User as tg_user


def create_user(effective_user: tg_user, chat_id: int) -> None:
    user = User(
        user_id=effective_user.id,
        first_name=effective_user.first_name,
        last_name=effective_user.last_name,
        username=effective_user.username,
        chat_id=chat_id,
        vacancy='None',
    )
    db_session.add(user)
    db_session.commit()
