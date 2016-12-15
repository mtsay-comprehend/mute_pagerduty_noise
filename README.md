# mute\_pagerduty\_noise
This script is a Selenium script to automate the browser and resolve PagerDuty
incidents considered noise by the user.

Every time you run this script, it will automate the browser to login into
PagerDuty, identify and select the incidents considered noise, and resolve
them.

One way to utilize this script is to set your PagerDuty notification rules to
notify you only after 10 minutes an incident has triggered and run this script
every 5 minutes.

# Dependencies
This script depends on python, Selenium, and Chrome driver. To install all
dependencies on OS X:

    brew install chromedriver python ; pip install selenium

# Usage
First go through `main.py` and update the script in sections marked by `TODO:`.

To run the script _once_, run `./main.py` in the terminal. This will trigger
the script to check PagerDuty _once_.

To run the script every 5 minutes, run the following in the terminal

    while true ; do ./main.py ; sleep 300 ; done

# TODOs
- figure out how to run Selenium in headless mode so we can turn this into a
  cronjob.
- externalize user credentials.
- externalize pattern matching.
