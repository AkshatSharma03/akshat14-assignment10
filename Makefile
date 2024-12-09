setup:
	pip install -r requirements.txt

run:
	python app.py

test:
	pytest

clean:
	rm -rf __pycache__ .pytest_cache
