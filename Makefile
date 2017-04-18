install:
	pip install -U flask
	pip install -U flask-cors

run:
	python server.py

test:
	tox -e py
.PHONY: test