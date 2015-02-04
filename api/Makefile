# Makefile for Flask simple api.
# Using Flask to make api for search.

.PHONY: all run test

# If you call make it just calls make run
all:
	$(MAKE) run

# Start Flask api
run:
	python $(ROOT_DIR)/api/run.py > api.log 2>&1 &
	@echo 'Flask api running!'

# Runs tests for API
test:
	@echo 'API Tests starting'
	python $(ROOT_DIR)/api/tests.py > api_test.log 2>&1 &
	@echo 'Tests finished'

