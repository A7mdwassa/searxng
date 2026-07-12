from waitress import serve
from searx.webapp import app
import os

if __name__ == '__main__':
    print("Starting SearXNG native Windows server on http://192.168.1.200:8888...")
    serve(app, host='0.0.0.0', port=8888, threads=12)
