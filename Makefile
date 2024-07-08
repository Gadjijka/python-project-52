start:
	gunicorn task_manager.wsgi:application

install:
	poetry install

lint:
	poetry run flake8 task_manager

test-coverage:
	poetry run coverage run manage.py test
	poetry run coverage report -m --include=task_manager/* --omit=task_manager/settings.py
	poetry run coverage xml --include=task_manager/* --omit=task_manager/settings.py

test:
	poetry run python3 manage.py test
