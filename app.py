from flask import Flask, render_template, jsonify
import json
import random

app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/projects')
def projects():
    projects_data = [
        {
            "name": "Client's Resume Website",
            "description": "Showcasing my client's research.",
            "progress": 10,
            "icon": "fa-solid fa-globe",
        },
        {
            "name": "VPN Service",
            "description": "A secure VPN for privacy.",
            "progress": 20,
            "icon": "fa-solid fa-shield-halved",
        },
        {
            "name": "PDF Extractor Revamp",
            "description": "Revamping the PDF Extractor project.",
            "progress": 55,
            "icon": "fa-solid fa-file-code",
        }
    ]
    return render_template('projects.html', projects=projects_data)

@app.route('/resume')
def resume():
    return render_template('resume.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/flashcards')
def flashcards():
    with open("flashcards.json", "r", encoding="utf-8") as file:
        flashcards = json.load(file)
    return render_template('flashcards.html', flashcards=flashcards)

@app.route('/get_flashcards')
def get_flashcards():
    with open("flashcards.json", "r", encoding="utf-8") as file:
        return jsonify(json.load(file))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)