all:
	pip install --user -r ./requirements.txt

# danger zone. Only do if you know what you're doing
clean:
	pip uninstall -r ./requirements.txt

test:
	python -m unittest discover -f -s tests -t .

lint:
	python -m black .
