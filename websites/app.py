from flask import Flask, send_from_directory

app = Flask(__name__, static_url_path='', static_folder='.')

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/<path:path>')
def static_files(path):
    return send_from_directory('../../AppData/Roaming/JetBrains/PyCharmEdu2022.2/scratches', path)

if __name__ == "__main__":
    app.run(debug=True)
