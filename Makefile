install:
	poetry install

gendiff:
	poetry run gendiff --help

build:
	poetry build

publish:
	poetry publish --dry-run

lint:
	poetry run flake8 brain_games

package-install:
	python3 -m pip install --user --force-reinstall dist/*.whl