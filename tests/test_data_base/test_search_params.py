from data_base.db import Base
from data_base.models import SearchParams
from data_base.search_params import create_search_params, get_search_params


def test__create_search_params(user_id, search_params):
    assert Base.db_session.query(SearchParams).count() == 0
    create_search_params(user_id, search_params)
    assert Base.db_session.query(SearchParams).count() == 1
    result = get_search_params(user_id)
    assert result == search_params


class TestGetSearhParams:
    def test__get_search_params_succes(self, user_id, search_params):
        result = get_search_params(user_id)
        assert result == search_params

    def test__get_search_params_not_found(self,):
        user_id = 5
        result = get_search_params(user_id)
        assert result is None
