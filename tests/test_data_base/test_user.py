from data_base.models import SearchParams, User
from data_base.user import (create_user, find_vacancy_name, is_user_in_db,
                            set_vacancy)


def test__create_user(effective_user):
    effective_user.id = 123
    chat_id = 111
    create_user(effective_user, chat_id)
    assert User.query.filter(User.user_id == effective_user.id).first()


class TestIsUserInDB:
    def test__is_user_in_db__true(self, effective_user):
        assert is_user_in_db(effective_user)

    def test__is_user_in_db__false(self, effective_user):
        effective_user.id = 12
        assert not is_user_in_db(effective_user)


def test__set_vacancy(effective_user, user_id):
    effective_user.id = user_id
    set_vacancy(effective_user, "test")
    assert SearchParams.query.filter(SearchParams.user_id == effective_user.id).first().vacancy_name == "test"


def test__find_vacancy_name(user_id):
    assert find_vacancy_name(user_id)
