# for helper functions throughout the app
import uuid
import os

def generate_unique_filename(filename):
    ext = filename.split('.')[-1]
    return f"{uuid.uuid4()}.{ext}"

