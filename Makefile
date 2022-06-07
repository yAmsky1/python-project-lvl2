install:
	poetry install

gendiff:
	poetry run gendiff --help

build:
	poetry build

publish:
	poetry publish --dry-run

lint:
	poetry run flake8 gendiff

test:
	poetry run pytest

test-cov:
	poetry run pytest --cov=gendiff --cov-report xml

package-reinstall:
	python3 -m pip install --user --force-reinstall dist/*.whl

package-install:
	python3 -m pip install --user dist/*.whl
