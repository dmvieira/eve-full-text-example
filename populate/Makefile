# Makefile for populate database.
# Populate database using HU scrapping.

.PHONY: all run

# If you call make it just calls make run
all:
	$(MAKE) run

# Start populate database action
run:
	python $(ROOT_DIR)/populate/run.py > populate.log 2>&1
	@echo 'Database populated!'
