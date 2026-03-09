import os

# Flask Configuration
UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads')
SECRET_KEY = 'your_secret_key_here'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}