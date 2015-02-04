# Stress test folder

Here we show results from stress test.

* All results are in results.html inside test folder.
* Some test details are in csv with all requests and agents that did request.
* Passed in tests with 12.000 requests/minute as detailed in results.html.
* Tested for 600 seconds.
* Tests was made using pylot 2.6 with the following command:
    
    python run.py -a 10 -r 10 -d 600 -n stress_test
