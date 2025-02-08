from flask import Flask, render_template

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
            "icon": "fa-solid fa-globe",  # Icon for website-related project
        },
        {
            "name": "VPN Service",
            "description": "A secure VPN for privacy.",
            "progress": 20,
            "icon": "fa-solid fa-shield-halved",  # Icon for security-related project
        },
        {
            "name": "PDF Extractor Revamp",
            "description": "Revamping the PDF Extractor project.",
            "progress": 55,
            "icon": "fa-solid fa-file-code",  # Icon for python-related project
        }
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