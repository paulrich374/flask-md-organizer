from flask import Flask, request, jsonify, send_from_directory, abort
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads/'

# Ensure the upload folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    file.save(os.path.join(UPLOAD_FOLDER, file.filename))
    return jsonify({'message': 'File uploaded successfully'}), 201

@app.route('/files', methods=['GET'])
def list_files():
    files = os.listdir(UPLOAD_FOLDER)
    return jsonify(files), 200

@app.route('/files/<filename>', methods=['GET'])
def view_file(filename):
    try:
        return send_from_directory(UPLOAD_FOLDER, filename)
    except FileNotFoundError:
        abort(404)

@app.route('/files/<filename>', methods=['DELETE'])
def delete_file(filename):
    try:
        os.remove(os.path.join(UPLOAD_FOLDER, filename))
        return jsonify({'message': 'File deleted successfully'}), 200
    except FileNotFoundError:
        abort(404)

if __name__ == '__main__':
    app.run(debug=True)