# Makefile for eve api.
# Using eve to make api for search.

.PHONY: all run

# If you call make it just calls make run
all:
	$(MAKE) run

# Start Eve api
run:
	python $(ROOT_DIR)/api/run.py > api.log 2>&1
	@echo 'Eve api running!'
