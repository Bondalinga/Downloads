from flask import Flask, send_from_directory, jsonify
import os

app = Flask(__name__, static_folder='C:/Users/kaide/Desktop/Website')

downloads_dir = 'C:/Users/kaide/Desktop/Website/downloads'

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/<path:path>')
def static_file(path):
    try:
        return app.send_static_file(path)
    except:
        return "File not found"

@app.route('/downloads/<path:path>')
def download_file(path):
    return send_from_directory(downloads_dir, path, as_attachment=True)

@app.route('/file-list')
def file_list():
    try:
        files = os.listdir(downloads_dir)
        return jsonify(files)
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    app.run(port=3000)
