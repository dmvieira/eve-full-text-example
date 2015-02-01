# Top-level Makefile for eve search example.
# Populate database, run apps, test code and uninstall.

ROOT_DIR = $(abspath ./)
export ROOT_DIR

include env_vars.mk

.PHONY: all run uninstall test populate

# If you call make it just calls make run
all:
	$(MAKE) run

# Restarts MongoDB using quiet mode
run:
	@echo 'Running MongoDB...'
	- killall mongod
	mongod --bind_ip $(MONGO_HOST) --port $(MONGO_PORT) --dbpath $(MONGO_PATH)/data/db/ --quiet

# Runs MongoDB and populate database scrapping Hotel Urbano
populate:
	@echo 'Running mongo for populate'
	$(MAKE) run &
	$(MAKE) run -C populate	

test:
	@echo 'doing'

# Remove MongoDB directory and uninstall all things
uninstall:
	rm -rf $(MONGO_PATH)
