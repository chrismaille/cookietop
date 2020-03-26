install:
	@poetry install
	rm -rf ./src

test:
	@poetry run pytest

format:
	@poetry run black .
