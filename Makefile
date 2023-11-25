SRC=oxygen.py
BIN_DIR=bin

PY=python3
PIP=pip3

REQ_SRC=requirements.txt

install:
	$(PIP) install -r $(REQ_SRC)

run:
	$(PY) $(SRC) --help
