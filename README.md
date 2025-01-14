# Clodpler
This module uses Python's `curl_cffi` to perform HTTP requests with support for Cloudflare-protected websites.

## Installation

```bash
git clone https://github.com/najibyahya/clodpler.git
```
```bash
cd clodpler
```
```bash
npm install
```
```
cd ..
```
```bash
pip install curl_cffi
```

## Runtutan Folder dan File
```
my-project/
├── node_modules/            # Dependencies project lainnya
├── clodpler/
│   ├── index.js
│   ├── package.json
│   └── python/
│       └── curl_wrapper.py
└── app.js                   # File utama anda untuk menjalankan program
```
## Contoh Penggunaan

```javascript
const { curlRequest } = require('my-nodejs-curl-module');

(async () => {
    try {
        const response = await curlRequest({
            method: 'GET',
            url: 'https://example.com',
            headers: {
                'User-Agent': 'MyApp',
            },
        });

        console.log('Status Code:', response.status_code);
        console.log('Headers:', response.headers);
        console.log('Response Body:', response.text);
    } catch (error) {
        console.error('Error:', error);
    }
})();
