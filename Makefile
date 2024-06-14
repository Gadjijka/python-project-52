start:
	python3 manage.py runserver

install:
	poetry install

lint:
	poetry run flake8 task_manager
