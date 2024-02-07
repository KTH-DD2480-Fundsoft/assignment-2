from ci_server.server import start_server
import unittest
from requests import post, get
from multiprocessing import Process 
import time 


class TestServer(unittest.TestCase):
    
    def setUp(self) -> None:
        self.ip = "0.0.0.0"
        self.port = 8027
        self.server = Process(target=start_server, args=(self.ip, self.port))
        self.server.start()
        time.sleep(1)        

    def test_webhook_json(self):
        payload = {"mol" : 42}
        response = post(f"http://{self.ip}:{self.port}/webhook",json=payload)
        self.assertTrue(response.ok, msg="server did not return OK status message.")
        try: 
            _ = response.json()
        except: 
            self.fail("response did not give valid JSON data.")

    def test_index(self):
        response = get(f"http://{self.ip}:{self.port}/")
        self.assertTrue(response.ok, msg="server did not return OK status message.")
    
    def tearDown(self) -> None:
        self.server.terminate()
        self.server.join()

