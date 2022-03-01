from app import app
from flask import render_template, request
import requests


@app.route('/', methods=['Get'])
def index():
    return render_template('index.html.j2')

@app.route('/properties', methods=['GET', 'POST'])
def properties():
    if request.method == 'POST':
        name = request.form.get('name')
        url = "https://pokeapi.co/api/v2/pokemon/" + f"{name.lower()}"
        response = requests.get(url)
        if response.ok:
            data = response.json()
            pokidata = {}
            pokidata = {
                'id': data['id'], 
                'name': data['name'].title(), 
                'weight': data['weight'], 
                'height': data['height'], 
                'types': data['types'], 
                'abilities': data['abilities'], 
                'stats': data['stats'],
                'default_sprite': data['sprites']['front_default'], 
                'shiny_sprite': data['sprites']['front_shiny']
            }
            return render_template('properties.html.j2', pokidata = pokidata)
        else:
            error_string = "Sorry Love, something went wrong."
            return render_template('properties.html.j2', error = error_string)
    error_string = "Please enter a Poki name or ID number."
    return render_template('properties.html.j2', error = error_string)