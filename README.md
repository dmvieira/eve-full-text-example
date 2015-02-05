# Text Search Example

Text search example using hotel urbano database and Flask framework

#Usage

Just execute these commands:

    git clone https://github.com/dmvieira/text-search-example.git
    cd text-search-example
    ./configure  # use bash
    make  # or make run (needs make installed)

I suggest you to use in virtualenv these commands.

These commands will configure your environment and start app. You need 
to define environment variables during configure command if these 
variables are not in your environment.

During configuration, it:

* Installs mongodb locally (no sudo need)
* Installs API
* Installs Interface
* Installs pip dependencies

## Populate

During populate it gets some Hotel Urbano database and insert in MongoDB. 
You can repeat the process running:

    make populate

You can configure how much data and other configs in populate/populate.cfg file.

## API

API works for Cities and Hotels, but you can just use GET feature. 

You can checkout log from server in api folder as .log file

### City

You can call city autocomplete API using:

    curl -i localhost:YOUR_PORT/city?name=can # here you will see all cities that starts with can as json

### Hotel

You can call hotel by city API using:

    curl -i localhost:YOUR_PORT/hotel?city_name=Arenal # here you will see all hotels in Arenal with can as json

## Interface

You can see interface accessing:
    
    http://localhost:INTERFACE_PORT

You can checkout log from server in interface folder as .log file

### Compile

Interface uses Jade and Scss for html and css respectively. You can run compile using:

    make compile

But compile occurs when you run automatically.

# Constraints Results

You can see constraint results for number of requests in tests/stress_test_results/results.html

The number tested was 12.000 reqs/min with Flask default server for API and Interface, but can handle much more with a better structure.

You can use Nginx for Interface to handle static files and Apache or Gunicorn to API, or you can use Nginx only as proxy reverse in Interface.

# Tests

You can run tests for API, Interface and PEP8 lint with:
    
    make test

You can checkout log from tests in .log files in each folder (api and interface).
