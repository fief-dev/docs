set dotenv-load := false

default:
  @just --list

install:
  python -m pip install --upgrade pip
  pip install -r requirements.txt
