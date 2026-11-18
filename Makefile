install:
	poetry install

test:
	poetry run pytest tests/unit

test-integration:
	poetry run pytest tests/integration

build:
	rm -rf ./dist && poetry build

publish:
	rm -rf ./dist && poetry publish --build
