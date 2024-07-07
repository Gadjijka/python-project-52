start:
	python3 manage.py runserver

install:
	poetry install

lint:
	poetry run flake8 task_manager

test-coverage:
	poetry run coverage manage.py test
	poetry run coverage report -m --include=task_manager/* --omit=task_manager/settings.py
	poetry run coverage xml --include=task_manager/* --omit=task_manager/settings.py

test:
	poetry run python3 manage.py test
