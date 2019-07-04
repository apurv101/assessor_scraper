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

import json
app = Flask(__name__)


firefox_path = "/Users/apoorv/Hausable/selenium_scraping/app/geckodriver"
chrome_path = "/Users/apoorv/Hausable/selenium_scraping/app/chromedriver"

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

        link_map = perform_scraping(address_string_a, "chrome", True, chrome_path, firefox_path)
        return make_response(jsonify(link_map))
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

        link_map = perform_scraping_san_mateo(address_string_a, "firefox", False, chrome_path, firefox_path)
        return make_response(jsonify(link_map))
    else:
        return make_response("test")

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    app.run(debug=True)

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=80)
    