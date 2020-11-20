venv:
	virtualenv venv; \

install:
	source venv/bin/activate; \
	pip install -r requirements.txt; \

clean:
	rm -rf venv
	find . -name "*.pyc" -delete