from flask import Flask, jsonify
from flask import abort
from flask import make_response
from flask import send_file
from flask import request
from scraping import perform_scraping
from scraping_sacramento import perform_scraping_sacramento
from scraping_san_francisco import perform_scraping_sfo
from scraping_san_mateo import perform_scraping_san_mateo
from scraping_la import perform_scraping_la
import threading
from multiprocessing import Pool
import json
import os
import logging
import sys


# Default daemon parameters.
# File mode creation mask of the daemon.
UMASK = 0

# Default working directory for the daemon.
WORKDIR = "/"

# Default maximum for the number of available file descriptors.
MAXFD = 1024

# The standard I/O file descriptors are redirected to /dev/null by default.
if (hasattr(os, "devnull")):
   REDIRECT_TO = os.devnull
else:
   REDIRECT_TO = "/dev/null"




# format = "%(asctime)s: %(message)s"

dir_path = os.path.dirname(os.path.realpath(__file__))
# print(dir_path + "/geckodriver_mac")
import platform

system = platform.system()
print(system)

app = Flask(__name__)

if system == "Darwin":
    firefox_path = dir_path + "/geckodriver_mac"
    chrome_path = dir_path + "/chromedriver_mac"
else:
    firefox_path = dir_path + "/geckodriver_linux"
    chrome_path = dir_path + "/chromedriver_linux"

print(firefox_path)
print(chrome_path)
# firefox_path = "/home/ubuntu/drivers/geckodriver"
# chrome_path = "/home/ubuntu/drivers/chromedriver"

@app.route('/get_image')
def get_image(image_link=None):
    return make_response("test")

@app.route('/alameda', methods = ['POST', 'GET'])
@app.route('/get_map', methods = ['POST', 'GET'])
def alameda():
    if request.method == 'POST':
        data = request.data
        address_string_a = json.loads(data)['address_string']
        # Start a worker processes
        pool = Pool(processes=1)              
        # Evaluate "f(10)" asynchronously calling callback when finished.
        pool.apply_async(perform_scraping, [address_string_a, "chrome", True, chrome_path, firefox_path]) 

        # logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
        # logging.info("Main    : before creating thread")
        # x = threading.Thread(target=perform_scraping, args=(address_string_a, "chrome", True, chrome_path, firefox_path,))
        # logging.info("Main    : before running thread")
        # x.start()
        # logging.info("Main    : wait for the thread to finish")
        # link_map = perform_scraping(address_string_a, "chrome", True, chrome_path, firefox_path)

        # return make_response(jsonify(link_map))
        print("OK")
        return "OK"
    else:
        return make_response("test")


@app.route('/sacramento', methods = ['POST', 'GET'])
def sacramento():
    if request.method == 'POST':
        data = request.data
        address_string_a = json.loads(data)['address_string']

        link_map = perform_scraping_sacramento(address_string_a, "firefox", True, chrome_path, firefox_path)
        return make_response(jsonify(link_map))
    else:
        return make_response("test")


@app.route('/san_francisco', methods = ['POST', 'GET'])
def san_francisco():
    if request.method == 'POST':
        data = request.data
        address_string_a = json.loads(data)['address_string']

        link_map = perform_scraping_sfo(address_string_a, "firefox", True, chrome_path, firefox_path)
        return make_response(jsonify(link_map))
    else:
        return make_response("test")

@app.route('/los_angeles', methods = ['POST', 'GET'])
def los_angeles():
    if request.method == 'POST':
        data = request.data
        address_string_a = json.loads(data)['address_string']

        link_map = perform_scraping_la(address_string_a, "chrome", True, chrome_path, firefox_path)
        return make_response(jsonify(link_map))
    else:
        return make_response("test")

@app.route('/san_mateo', methods = ['POST', 'GET'])
def san_mateo():
    if request.method == 'POST':
        data = request.data
        address_string_a = json.loads(data)['address_string']

        pool = Pool(processes=1)              
        # Evaluate "f(10)" asynchronously calling callback when finished.
        pool.apply_async(perform_scraping_san_mateo, [address_string_a, "chrome", True, chrome_path, firefox_path]) 

        # link_map = perform_scraping(address_string_a, "chrome", True, chrome_path, firefox_path)

        # return make_response(jsonify(link_map))
        print("OK")
        return "OK"
    else:
        return make_response("test")

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    if system == "Darwin":
        app.run(debug=True)
    else:
        app.run(host='0.0.0.0', port=80)

# if __name__ == '__main__':
#     
    