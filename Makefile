install:
	pip install -r requirements.txt

run:
	flask --app api.src.app run --debug

tree:
	tree -a -I ".venv|.git"

migrate:
	python -m shared.migrations