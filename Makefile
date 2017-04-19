install:
	pip install -U flask
	pip install -U flask-cors

run:
	python server.py

test:
	python setup.py test
.PHONY: test
