from flask import Flask
from flask import request

import folium
import geocoder
from flask import render_template


app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template('main.html')


@app.route('/handle_data', methods=['POST'])
def location():
    ip_address = request.form['ip_address']
    g = geocoder.ip(ip_address)
    response = g.response.status_code
    if response != 200:
        return render_template('error.html')
    myAddress = g.latlng
    mymap1 = folium.Map(location=myAddress, zoom_start=12)
    mymap1.save("templates/map.html")
    return render_template('map.html')


if __name__ == "__main__":
    app.run(debug=True)
