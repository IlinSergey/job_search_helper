IGNORE_DIR = env .pytest_cache .mypy_cache __pycache__ .vscode


FLAKE8_FLAGS = --exclude=$(IGNORE_DIR)


style:
	flake8 $(FLAKE8_FLAGS)

types:
	mypy .

tests:
	pytest .

check:
	make -j3 style types tests
