from flask import Flask, render_template,request,jsonify,Response  
import sys
import os
import warnings
import logging
import urllib3
import json
import requests
from flask_cors import CORS
import time
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import threading
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(root_dir)


from api.hf import *



app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 100 * 1024 * 1024
CORS(app)
warnings.filterwarnings("ignore", category=urllib3.exceptions.InsecureRequestWarning)

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
logging.getLogger("urllib3").setLevel(logging.CRITICAL)
logging.getLogger("requests").setLevel(logging.CRITICAL)


total = 0
pending = 0
lock = threading.Lock()

@app.route("/")
def index():
  message = f"total requests : {total} \n pending requests : {pending} "
  return message


@app.route("/test")
def test():
    proxy = WorkingProxy()
    proxy = {
        'http': proxy,
        'https': proxy
    }
    r = requests.get('https://httpbin.org/ip',proxies=proxy,verify=False)
    return jsonify({"r": r.json(),"p": proxy})
@app.route("/test1")
def test1():
    proxy = WorkingProxy()
    
    return jsonify({"p": proxy})



@app.route('/hf/img/gen', methods=['POST'])
def Hf():
    with lock:
        global total, pending
        total += 1
        pending += 1
    prompt = request.json.get('prompt', '')
    negative = request.json.get('negative', '')
    steps = request.json.get('steps', 20)
    width = request.json.get('width',1024)
    height = request.json.get('height',1024)
    scale = request.json.get('scale',7)
    model = request.json.get('model','sd3')
    style = request.json.get('style', 'Cinematic')
    shash = request.json.get('hash')
    if model == 'rvs4':
        def generator():
            global pending
            while True:  
                try:
                    for info in rvx(prompt=prompt, negative=negative, width=width, height=height, scale=scale, steps=steps, style=style, shash=shash):
                        if "error" in json.dumps(info):
                            raise ValueError("Error in response, retrying...")
                        else:
                            yield f'data: {json.dumps(info)}\n\n'
                    pending -= 1
                    break 
                except ValueError as e:
                    continue  
        return Response(generator(), mimetype="text/event-stream")

    

    elif model == 'mobius':
        def generator():
            global pending
            while True:  
                try:
                    for info in mobius(prompt=prompt, negative=negative, width=width, height=height, scale=scale, steps=steps, style=style, shash=shash):
                        if "error" in json.dumps(info):
                            raise ValueError("Error in response, retrying...")
                        else:
                            yield f'data: {json.dumps(info)}\n\n'
                    pending -= 1
                    break 
                except ValueError as e:
                    continue  
        return Response(generator(), mimetype="text/event-stream")
    
    elif model == 'sd3':
        def generator():
            global pending
            while True:  
                try:
                    for info in sd3(prompt=prompt, negative=negative, width=width, height=height, scale=scale, steps=steps, style=style, shash=shash):
                        if "error" in json.dumps(info):
                            raise ValueError("Error in response, retrying...")
                        else:
                            yield f'data: {json.dumps(info)}\n\n'
                    pending -= 1
                    break 
                except ValueError as e:
                    continue  
        return Response(generator(), mimetype="text/event-stream")
        
        return Response(generator(), mimetype="text/event-stream")
    
    elif model == 'sdflash':
        def generator():
            global pending
            while True:  
                try:
                    for info in sdflash(prompt=prompt, negative=negative, width=width, height=height, scale=scale, steps=steps, style=style, shash=shash):
                        if "error" in json.dumps(info):
                            raise ValueError("Error in response, retrying...")
                        else:
                            yield f'data: {json.dumps(info)}\n\n'
                    pending -= 1
                    break 
                except ValueError as e:
                    continue  
        return Response(generator(), mimetype="text/event-stream")

  
    elif model == 'kivotos':
        def generator():
            global pending
            while True:  
                try:
                    for info in kivotos(prompt=prompt, negative=negative, width=width, height=height, scale=scale, steps=steps, style=style, shash=shash):
                        if "error" in json.dumps(info):
                            raise ValueError("Error in response, retrying...")
                        else:
                            yield f'data: {json.dumps(info)}\n\n'
                    pending -= 1
                    break 
                except ValueError as e:
                    continue  
        return Response(generator(), mimetype="text/event-stream")
        
    elif model == 'OpenDalle':
        def generator():
            global pending
            while True:  
                try:
                    for info in OpenDalle(prompt=prompt, negative=negative, width=width, height=height, scale=scale, steps=steps, style=style, shash=shash):
                        if "error" in json.dumps(info):
                            raise ValueError("Error in response, retrying...")
                        else:
                            yield f'data: {json.dumps(info)}\n\n'
                    pending -= 1
                    break 
                except ValueError as e:
                    continue  
        return Response(generator(), mimetype="text/event-stream")
        
    else:
        pending-=1
        return jsonify('model not found'), 404


if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=7860)
