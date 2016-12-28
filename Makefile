setup: venv
	venv/bin/pip install --upgrade pip==9.0.1
	venv/bin/pip install -e .
	venv/bin/pip install -r test_requirements.txt
venv:
	python3.5 -m venv venv
