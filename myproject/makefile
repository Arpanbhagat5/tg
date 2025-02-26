.PHONY: up migrate loaddata restart test-be

up:
	docker-compose up --build -d

migrate:
	docker-compose exec django python manage.py showmigrations
	docker-compose exec django python manage.py migrate
	docker-compose exec django python manage.py showmigrationsl

# use this to load data from fixtures
loaddata:
	docker-compose exec django python manage.py loaddata backend/fixtures/prefectures.json

# use this to create a superuser and check data in admin console
create-superuser:
	docker-compose exec django python manage.py createsuperuser --username admin --email amdin@tg.com

# Restart the backend and DB
restart:
	docker-compose down && docker-compose up --build -d

# Run the backend tests
test-be:
	docker-compose exec django python manage.py test

# Format the code using black and isort
format:
	docker-compose exec django black . --line-length 88
	docker-compose exec django isort . --profile black

# Lint the code using ruff and pylint
lint:
	docker-compose exec django ruff check .

# Check all linters and formatters
check: lint format