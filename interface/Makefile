# Makefile for flask interface.
# Using flask to make simple interface for search.

SCSS_DIR=$(ROOT_DIR)/interface/app/assets/scss
CSS_DIR=$(ROOT_DIR)/interface/app/static/css

JADE_DIR=$(ROOT_DIR)/interface/app/assets/jade
HTML_DIR=$(ROOT_DIR)/interface/app/templates

.PHONY: all run compile test

# If you call make it just calls make run
all:
	$(MAKE) run

# Compiles jade and scss files
compile:
	pyjade -c jinja $(JADE_DIR)/index.jade $(HTML_DIR)/index.html
	pyscss $(SCSS_DIR)/style.scss -o $(CSS_DIR)/style.css

# Starts Flask interface
run:
	$(MAKE) compile
	python $(ROOT_DIR)/interface/run.py > interface.log 2>&1 &
	@echo 'Flask Interface running!'

# Runs tests for interface
test:
	python $(ROOT_DIR)/interface/tests.py > interface_test.log 2>&1 &
	
