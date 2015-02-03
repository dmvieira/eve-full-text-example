# Top-level Makefile for eve search example.
# Populate database, run apps, test code, compile jade and scss and uninstall.

ROOT_DIR = $(abspath ./)
export ROOT_DIR

include env_vars.mk

.PHONY: all run uninstall test populate compile

# If you call make it just calls make run
all:
	$(MAKE) run

# Restarts MongoDB using quiet mode
database_restart:
	@echo 'Running MongoDB...'
	- mongod --shutdown --dbpath $(MONGO_PATH)/data/db/
	mongod --bind_ip $(MONGO_HOST) --port $(MONGO_PORT) --dbpath $(MONGO_PATH)/data/db/ --quiet > mongod.log 2>&1

# Runs database, api and interface
run:
	$(MAKE) database_restart &
	@echo 'Running Eve Api...'
	$(MAKE) run -C api &
	@echo 'Running Flask Interface'
	$(MAKE) run -C interface
	@echo "Service API running in port $(API_PORT) and Interface in port $(INTERFACE_PORT)"

# Runs MongoDB and populate database scrapping Hotel Urbano
populate:
	@echo 'Running mongo for populate'
	$(MAKE) database_restart &
	$(MAKE) run -C populate	

test:
	@echo 'doing'

# Compiles interface scss and jade
compile:
	$(MAKE) compile -C interface

# Remove MongoDB directory and uninstall all things
uninstall:
	- rm -rf $(MONGO_PATH)
	- rm -f env_vars.mk
