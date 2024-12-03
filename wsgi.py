import sys
from os.path import dirname, join

sys.path.insert(0, dirname(__file__))

from app import app  # Replace 'your_app' with your actual app module name

if __name__ == "__main__":
    app.run()