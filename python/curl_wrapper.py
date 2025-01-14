import sys
import json
from curl_cffi import requests

def main():
    # Baca input JSON dari Node.js
    input_data = sys.stdin.read()
    params = json.loads(input_data)

    try:
        if params['method'].lower() == 'get':
            response = requests.get(params['url'], headers=params.get('headers', {}))
        elif params['method'].lower() == 'post':
            response = requests.post(params['url'], headers=params.get('headers', {}), data=params.get('data', {}))
        else:
            print(json.dumps({"error": "Unsupported method"}))
            return

        # Kembalikan hasil sebagai JSON
        print(json.dumps({
            "status_code": response.status_code,
            "headers": dict(response.headers),
            "text": response.text
        }))
    except Exception as e:
        print(json.dumps({"error": str(e)}))

if __name__ == '__main__':
    main()
