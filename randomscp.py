# Imports #

from flask import Flask
from requests import get
import random


# Get the current series #
def get_series():
    cs = 2 # Current series
    # Starts at 2 because the link for the first series does not have a digit after it
    stillvalid = True
    while stillvalid:
        # Keep increasing cs until Series cs doesn't exist
        if get("http://www.scpwiki.com/scp-series-" + str(cs)).status_code == 404:
            # If series doesn't exist, go back one and that will
            # give you the current series.
            cs -= 1
            return cs
        else:
            cs += 1

# Get the SCP number and make sure it exists #
def get_random_number():
    get404 = True
    while get404:
        num = random.randint(1, (get_series() * 1000) - 1)
        num_str = ""
        # Should I remove this or will num_str only be defined in the if statements?
        if len(str(num)) == 1:
            num_str = "00" + str(num)
        elif len(str(num)) == 2:
            num_str = "0" + str(num)
        else:
            num_str = str(num)
        if get("http://www.scpwiki.com/scp-" + num_str).status_code != 404:
            # If the request doesn't 404, that's the SCP we're using
            return num_str

# Set up Flask #
app = Flask(__name__)


@app.route('/')
def random_scp():
    # Create a script tag that redirects the user to the random SCP page #
    return """
    <script>
    window.location.href = 'http://www.scpwiki.com/scp-""" + get_random_number() + """'
    </script>
    """
