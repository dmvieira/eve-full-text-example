# Top-level Makefile for eve search example.
# Populate database, run apps, test code and uninstall.

ROOT_DIR = $(abspath ./)
export ROOT_DIR

include env_vars.mk

.PHONY: all run uninstall test populate

all:
	$(MAKE) run

run:
	@echo 'Running MongoDB...'
	- killall mongod
	mongod --bind_ip $(MONGO_HOST) --port $(MONGO_PORT) --dbpath $(MONGO_PATH)/data/db/ --quiet

populate:
	@echo 'Running mongo for populate'
	$(MAKE) run & 
	python $(ROOT_DIR)/config/populate.py
	@echo 'Database populated!'

test:
	@echo 'doing'

uninstall:
	rm -rf $(MONGO_PATH)
