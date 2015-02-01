# Top-level Makefile for eve search example.
# Populate database, run apps, test code and uninstall.

ROOT_DIR = $(abspath ./)
export ROOT_DIR

include env_vars.mk

.PHONY: all run uninstall test populate

all:
	$(MAKE) run

run:
	@echo 'doing'

populate:
	@echo 'doing'

test:
	@echo 'doing'

uninstall:
	rm -rf $(MONGO_PATH)
