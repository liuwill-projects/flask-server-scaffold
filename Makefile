install:
	pip install -f requirements.txt

run:
	python main.py

test:
	python setup.py test
.PHONY: test
