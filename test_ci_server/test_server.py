import os
import unittest
from multiprocessing import Process 
import time 


class TestServer(unittest.TestCase):
    '''
        Class containing tests for the flask server in `ci_server/server.py`.
    '''

    @classmethod
    def setUpClass(cls) -> None:
        '''
            Hook method for setting up class fixture before running tests in the class.

            Parameters
            ----------
            TODO: Add parameter type.
            `cls` : (`?`)
                TODO: Write explanation.
        '''

        cls.ip = "0.0.0.0"
        cls.port = 5000 
        
        cls.webhook_addr = f"http://{cls.ip}:{cls.port}/webhook"
        cls.index_addr = f"http://{cls.ip}:{cls.port}/"
        
        cls.old_authkey = os.getenv("FLASK_AUTHKEY")
        cls.new_authkey = "123456789"
        os.environ["FLASK_AUTHKEY"] = cls.new_authkey
        
        cls.old_testing = os.getenv("FLASK_TESTING")
        os.environ["FLASK_TESTING"] = "true" 
        
        from ci_server.server import start_server, app
        
        cls.app = app  
        cls.server = Process(target=start_server, args=(cls.ip, cls.port))
        cls.server.start()
        time.sleep(1)  
    
    @property 
    def valid_authkey(self):
        '''
            TODO: Write explanation.

            Parameters
            ----------

            Returns
            -------
            `self.new_authkey` : (`str`)
                TODO: Write explanation.
        '''

        return self.new_authkey

    @property 
    def invalid_authkey(self): 
        '''
            TODO: Write explanation.

            Parameters
            ----------

            Returns
            -------
            `letmein` : (`str`)
                The string `"letmein"`
        '''

        return "letmein"
    
    @property
    def valid_data(self):
        '''
            TODO: Write explanation.

            Parameters
            ----------

            Returns
            -------
            data : (`dict`)
                A dictionary containing branch, commit, and push info.
        '''

        data = {} 
        data['ref'] = "ref/this/branch/doesnt/exist"
        data['head_commit'] = {
            "id" : "123",
            "author" : "John Doe",
            "timestamp" : "2000-10-31T01:30:00.000+01:00"
        }
        data['pusher'] = { "name" : "Jane Doe" }
        return data

    def test_webhook_bad_authkey(self):
        '''
            Tests that an invalid `AUTH_KEY` results in a HTTP `401` response code.
        '''

        headers = {"X-Hub-Signature-256" : self.invalid_authkey}
        with self.app.test_client() as client: 
            response = client.post(self.webhook_addr, json={}, headers=headers)
            self.assertTrue(response.status_code == 401, 
                            msg=f"Expected HTTP 401 for bad authkey, got {response.status_code}")
    
    def test_webhook_bad_json(self):
        '''
            Tests that a webhook request with a valid `AUTH_KEY` but invalid JSON results 
            in a HTTP `400` response code.
        '''

        payload = {"mol" : 42}
        headers = {"X-Hub-Signature-256" : self.valid_authkey}
        with self.app.test_client() as client:
            response = client.post(self.webhook_addr,json=payload, headers=headers)
            self.assertTrue(response.status_code == 400, 
                            msg=f"Expected HTTP 400 for bad json, got {response.status_code}")
    
    def test_webhook(self):
        '''
            Tests that posting a valid webhook request results in a HTTP 202 response code.
        '''

        headers = {"X-Hub-Signature-256" : self.valid_authkey}
        with self.app.test_client() as client:
            response = client.post(self.webhook_addr,
                            json=self.valid_data,
                            headers=headers)
            self.assertTrue(response.status_code == 202,
                            msg=f"Expected HTTP 202, got {response.status_code}") 

    def test_index(self):
        ''' 
            Tests that doing a get request for the index address results in a
            HTTP `200` response code.
        '''

        with self.app.test_client() as client:
            response = client.get(self.index_addr)
            self.assertTrue(response.status_code == 200, 
                            msg=f"Expected HTTP 200, got {response.status_code}")
            
    @unittest.skipIf(not os.path.isdir('build_history'), 
                     "Build history directory not found. Skipping test.")
    def test_build_history_urls(self):
        '''
            Tests that each file in build_history has a valid URL that is equal 
            to its file name. Does this by performing a get request for each url
            and verifying that it returns a HTTP `200` response code. This test
            is skipped if the build_history directory doesn't exist.
        '''

        # Get all filenames in build_history
        build_history_names = [f for f in os.listdir('build_history') 
                               if os.path.isfile(os.path.join('build_history', f))]

        with self.app.test_client() as client:
            for name in build_history_names:
                url = self.index_addr + "/build_history/" + name
                response = client.get(url)
                self.assertTrue(response.status_code == 200, 
                                msg=f"Expected HTTP 200, got {response.status_code}")
    
    @classmethod
    def tearDownClass(cls) -> None:
        '''
            Hook method for deconstructing the class fixture after running all tests in the class.

            Parameters
            ----------
            TODO: Add parameter type.
            `cls` : (`?`)
                TODO: Write explanation.
        '''

        cls.server.terminate()
        cls.server.join()
        time.sleep(1)
        os.environ["FLASK_AUTHKEY"] = cls.old_authkey if cls.old_authkey else ""
        os.environ["FLASK_TESTING"] = cls.old_testing if cls.old_testing else ""
        return 

