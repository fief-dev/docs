set dotenv-load := false

examples_python_bin := "./examples/python/venv/bin/python"

default:
  @just --list

install:
  python -m pip install --upgrade pip
  pip install -U -r requirements.txt

examples-python *ARGS:
  {{examples_python_bin}} {{ARGS}}

examples-python-install:
  if [ ! -d "examples/python/venv" ]; then python -m venv examples/python/venv; fi
  {{examples_python_bin}} -m pip install --upgrade pip
  {{examples_python_bin}} -m pip install -r examples/python/requirements.txt

examples-python-lint:
  {{examples_python_bin}} -m isort --profile black examples/python
  {{examples_python_bin}} -m black examples/python
  {{examples_python_bin}} -m tryceratops --exclude examples/python/venv/ examples/python
  {{examples_python_bin}} -m mypy --exclude venv/ examples/python
