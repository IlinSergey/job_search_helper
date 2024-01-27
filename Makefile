SRC_DIR = .
IGNORE_DIR = env .pytest_cache .mypy_cache __pycache__ .vscode

TEST_DIR = tests

MYPY_FLAGS = --ignore-missing-imports
FLAKE8_FLAGS = --exclude=$(IGNORE_DIR)


style:
	flake8 --exclude=migrations,env,.pytest_cache,.mypy_cache,__pycache__,.vscode $(SRC_DIR)

types:
	mypy $(MYPY_FLAGS) $(SRC_DIR)

tests:
	pytest $(SRC_DIR) $(TEST_DIR) --ignore=$(IGNORE_DIR)

check:
	make -j3 style types tests
