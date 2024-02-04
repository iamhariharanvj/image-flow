from flask import Flask, render_template, url_for
import firebase_admin
from firebase_admin import credentials, storage
import os
from dotenv import load_dotenv

load_dotenv()

cred = credentials.Certificate(os.getenv("GOOGLE_APPLICATION_CREDENTIALS"))
firebase = firebase_admin.initialize_app(cred, {
    "storageBucket": os.getenv("STORAGE_BUCKET")
})
bucket = storage.bucket()

app = Flask(__name__, template_folder='')

local_folder = os.path.join(app.root_path, 'static', 'downloaded_files')

@app.route('/')
def index():
    blobs = list(bucket.list_blobs())

    os.makedirs(local_folder, exist_ok=True)

    for blob in blobs:
        destination_file = os.path.join(local_folder, blob.name)
        blob.download_to_filename(destination_file)

    blobs_paths = [url_for('static', filename=f'downloaded_files/{blob.name}') for blob in blobs]

    return render_template('./index.html', images=blobs_paths)

if __name__ == '__main__':
    app.run(debug=True)
