from flask import Flask, send_file, render_template, request, redirect, session, url_for
from user_agents import parse
import os

app = Flask(__name__)


# Définir une fonction pour détecter si la résolution de l'appareil est mobile
def is_mobile():
    user_agent = parse(request.headers.get('User-Agent'))
    return user_agent.is_mobile


@app.route('/')
def home():
    """ if is_mobile():
        return redirect(url_for('phone_home')) """
    return render_template('/pages/home.html')


@app.route('/phone_home')
def phone_home():

    return render_template('/phone/phone-home.html')


@app.route('/phone_iot')
def phone_iot():
    return render_template('/phone/phone_iot.html')


@app.route('/phone_ftth')
def phone_ftth():
    return render_template('/phone/phone_ftth.html')


@app.route('/phone_contact')
def phone_contact():
    return render_template('/phone/phone_contact.html')


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
    app.run(host="0.0.0.0", debug=True, port=9001)
