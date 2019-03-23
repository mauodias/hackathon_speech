venv_path ?=.venv
source_venv =. $(venv_path)/bin/activate &&

venv:
	test -d $(venv_path) || python3 -m venv $(venv_path)

run: venv
	$(source_venv) python speech.py
