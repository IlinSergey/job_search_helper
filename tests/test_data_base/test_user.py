import pytest

from data_base.models import User
from data_base.user import create_user


@pytest.mark.run()
def test__create_fake_user(effective_user):
    effective_user.id = 123
    chat_id = 111
    create_user(effective_user, chat_id)
    assert User.query.filter(User.user_id == effective_user.id).first()
