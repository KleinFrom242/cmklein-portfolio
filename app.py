from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/projects')
def projects():
    projects_data = [
        {"name": "Sister’s Resume Website", "description": "Showcasing my sister’s research.", "progress": 10},
        {"name": "VPN Service", "description": "A secure VPN for privacy.", "progress": 20},
    ]
    return render_template('projects.html', projects=projects_data)

@app.route('/resume')
def resume():
    return render_template('resume.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)