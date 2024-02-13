import os
from ci_server import log
from flask import Flask, request 
from datetime import datetime
from ci_server.ci_runner import continuous_integration 
from multiprocessing import Process
from flask_autoindex import AutoIndex

import json

# for verifying signature
import hashlib
import hmac

def verify_signature(payload_body, secret_token, headers):
    """Verify that the payload was sent from GitHub by validating SHA256.

    Raise and return 403 if not authorized.

    Args:
        payload_body: original request body to verify (request.body())
        secret_token: GitHub app webhook token (WEBHOOK_SECRET)
        signature_header: header received from GitHub (x-hub-signature-256)
    """
       
    if "X-Hub-Signature-256" not in headers:
        return False
    
    hash_object = hmac.new(secret_token.encode('utf-8'), msg=payload_body, digestmod=hashlib.sha256)
    expected_signature = "sha256=" + hash_object.hexdigest()
    if not hmac.compare_digest(expected_signature, headers["X-Hub-Signature-256"]):
        return False
    return True


UNAUTHORIZED = ("unauthorized", 401)
BAD_REQUEST  = ("bad request" , 400)
INTERNAL_ERROR = ("internal error", 500)

app = Flask(__name__)
app.config.from_prefixed_env(loads=lambda x: x)

build_path = "./build_history" # Relative path to the build history directory

# Show the files in the build history directory
AutoIndex(app, browse_root=build_path) 

assert app.config["AUTHKEY"], "No authkey in ENV"

@app.route('/webhook', methods=['POST'])
def webhook():
    '''
        See flask docs: https://flask.palletsprojects.com/en/latest/quickstart/#routing
        
        This function is run when there is a HTTP request directed at this server at 
        route `/webhook`, so if our server is at example.org. This is run when someone
        accesses example.org/webhook.

        We only want to deal with GitHub webhooks, more specifically, only push and release
        events. See:
        
        `This <https://docs.github.com/en/webhooks/webhook-events-and-payloads#push/>`_
        and `this <https://docs.github.com/en/webhooks/webhook-events-and-payloads#release/>`_ 
        respectively.

        Parameters
        ----------

        Returns
        ----------
        `response` : (`response`)
            See: https://flask.palletsprojects.com/en/latest/quickstart/#about-responses
            
            The return value -- if valid -- is automatically converted to a response object,
            a bad response must therefore be specified by returning a tuple, where the second
            element is the return code.

            This function, however, should only return JSON and a return-code.
    '''

    log.info(f"New webhook from {request.remote_addr}")
    
    data = request.data

    # Make sure the authkey is correct.
    authkey = app.config["AUTHKEY"]
    authorized = verify_signature(data, authkey, request.headers)
    if not authorized:
        log.error(f"Invalid secret key from {request.remote_addr}")
        return UNAUTHORIZED
    
    # Try to get all the data needed
    try:
        data = json.loads(data.decode())
        ref           = data['ref']
        commit_id     = data['head_commit']['id']
        timestamp     = datetime.fromisoformat(data['head_commit']['timestamp'])
        commit_author = data['head_commit']['author']
        pusher        = data['pusher']['name'] 
    
   # All the above data is required, bad data otherwise
    except KeyError as e:
        log.error(str(e))
        return BAD_REQUEST 
    except ValueError as e:
        log.error(str(e))
        return BAD_REQUEST 
    # Any other exception is a server error
    except Exception as e:
        log.error("unhandled exception: " + str(e))
        return INTERNAL_ERROR
    
    log.info(f"""Received CI webhook from {request.remote_addr}
    ref: {ref}
    commit: 
        id: {commit_id}
        timestamp {timestamp.timestamp}    
        author: {commit_author}
    pusher: {pusher}""")
    
    if not app.config['TESTING']:
        # Fire and forget. Not tested when testing the server, we have seperate
        # unittests for this.
        ci_process = Process(target=continuous_integration, args=(commit_id,))
        ci_process.start()

    return {"response" : "thanks!"}, 202 

@app.route('/', methods=['GET'])
def index():
    ''' 
        See flask docs: https://flask.palletsprojects.com/en/latest/quickstart/#routing
        
        This function is run when there is a HTTP request directed at this server at 
        route `/`, i.e., at the index, so if our server is at example.org. This is run 
        when someone accesses example.org/ -- the 'home page'.

        Parameters
        ----------

        Returns
        ----------
        `response` : (`response`)
            See: https://flask.palletsprojects.com/en/latest/quickstart/#about-responses
            
            The return value -- if valid -- is automatically converted to a response object,
            a bad response must therefore be specified by returning a tuple, where the second
            element is the return code.

            This function, however, should only return text/html and a return-code.
    ''' 
    return (""" 
<h1> Under construction </h1>

<br>

<svg version="1.1" id="Layer_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 250 250" style="enable-background:new 0 0 122.88 111.6" xml:space="preserve"><style type="text/css">.st0{fill-rule:evenodd;clip-rule:evenodd;}</style><g><path class="st0" d="M56.72,0c6.88,0,12.46,5.58,12.46,12.46c0,6.88-5.58,12.46-12.46,12.46s-12.46-5.58-12.46-12.46 C44.26,5.58,49.84,0,56.72,0L56.72,0z M66.59,104.89c1.97-3.61,3.77-6.89,5.86-10.12c2.09-3.23,4.46-6.39,7.56-9.76l0.92-0.96 L47.29,69.17l8.42,13.33c0.69,1.09,0.98,2.31,0.92,3.51l-0.84,17.31c-0.16,3.34-2.99,5.91-6.32,5.76 c-3.34-0.16-5.91-2.99-5.76-6.32l0.75-15.42l-11.81-18.7l-8,34.79c-0.75,3.26-3.99,5.29-7.25,4.55c-3.26-0.75-5.29-3.99-4.55-7.25 l9.77-42.47L0,48.18l1.77-9.5l5.46,2.41l6.4-11.32c0.93-1.64,2.52-2.68,4.24-2.98l0-0.01L35.8,23.7c1.29-0.22,2.55-0.02,3.65,0.51 l22,9.37c1.88,0.8,3.14,2.44,3.54,4.29l0.01,0l6.6,30.32c0.1,0.48,0.15,0.96,0.14,1.43l16.15,7.14l11.18-11.7L99.18,65l0.18-0.05 c10.86-2.65,20.11,28.66,21.93,36.12l0.17,0.72c1.35,5.51,1.94,7.93,0.84,9.04c-0.86,0.87-2.67,0.81-5.89,0.72 c-1.49-0.04-3.29-0.1-5.44-0.07c-6.77,0.07-13.44,0.07-19.99-0.04c-6.55-0.1-12.97-0.3-19.23-0.6c-1.55-0.08-2.82-0.08-3.84-0.09 c-1.91-0.01-2.97-0.02-3.39-0.49c-0.55-0.62,0.08-1.75,1.48-4.29L66.59,104.89L66.59,104.89z M33.33,36.41L26.92,49.8L18.34,46 l4.39-7.77L33.33,36.41L33.33,36.41z M49.24,59.67l5.17-13.52l3.81,17.49L49.24,59.67L49.24,59.67z"/></g></svg>

<br>
        """, 200)

def start_server(ip,port):
    """
        Runs the server at the IP `ip` and the port `port`.

        Parameters
        ----------
        `ip` : (`str`)
            The IP at which the server should run.
        `port` : (`int`)
            The port number at which the server should run.
    """
    
    app.run(host=ip,port=port)
