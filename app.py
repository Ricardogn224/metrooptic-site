from flask import Flask, send_file, render_template, request, redirect, session, url_for
import os

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('/pages/home.html')


@app.route('/FTTH_pro')
def ftth_pro():
    return render_template('/pages/FTTH_pro.html')


@app.route('/FTTH_pro_secure')
def ftth_pro_secure():
    return render_template('/pages/FTTH_pro_secure.html')


@app.route('/FTTO_pro')
def ftto_pro():
    return render_template('/pages/FTTO_pro.html')


@app.route('/FTTO_pro_secure')
def ftto_pro_secure():
    return render_template('/pages/FTTO_pro_secure.html')


@app.route('/iot')
def iot():
    return render_template('/pages/solution-iot.html')


@app.route('/contact')
def contact():
    return render_template('/pages/contact.html')


@app.route('/solution_data')
def data():
    return render_template('/pages/4G_5G.html')


@app.route('/data_center')
def data_center():
    return render_template('/pages/data-center.html')


@app.route('/secutite')
def securite():
    return render_template('/pages/securite.html')


@app.route('/secutite_ultra')
def securite_ultra():
    return render_template('/pages/securite_ultra.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=7001)
