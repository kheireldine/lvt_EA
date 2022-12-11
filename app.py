from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import requests, uuid, json

import os
import time
from multiprocessing.pool import ThreadPool
from azure.storage.blob import BlobServiceClient, BlobClient
from azure.storage.blob import ContentSettings, ContainerClient
import numpy as np
from datetime import datetime, timedelta
app = Flask(__name__)
from pydub import AudioSegment
from pydub.utils import make_chunks
import os










@app.route('/')
def upload_file1():
    return render_template('index.html')


@app.route('/uploader', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename(f.filename))
        print(f.filename)

        return  f.filename
    else:
        return "Hello World"

if __name__ == '__main__':
    app.run(debug=True)
