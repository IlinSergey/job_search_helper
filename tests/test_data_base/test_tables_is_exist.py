from data_base.db import Base


def test__tables_is_exist():
    assert Base.metadata.tables.keys() == {"users", "vacanciens", "search_params"}
