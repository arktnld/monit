import http.client
import json
from urllib.parse import urlparse
import time

class HTTPClient():
    @staticmethod
    def request(url, data_json):
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }
        parsed_url = urlparse(url)
        host = parsed_url.netloc
        path = parsed_url.path if parsed_url.path else "/"

        connection = http.client.HTTPSConnection(host)
        headers.update({'Content-type': 'application/json'})

        query_json = json.dumps(data_json)
        for _ in range(3):  # Three attempts
            try:
                connection.request("POST", path, query_json, headers)
                response = connection.getresponse()
                data = response.read().decode("utf-8")
                response_json = json.loads(data)
                connection.close()
                return response_json
            except Exception as e:
                print(f"HTTP request failed: {e}")
                print("Retrying...")
                time.sleep(5)  # Wait for 5 seconds before retrying
        raise ValueError("HTTP request failed after multiple attempts")
