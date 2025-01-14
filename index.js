const { PythonShell } = require('python-shell');
const path = require('path');

function curlRequest({ method, url, headers = {}, data = {} }) {
    return new Promise((resolve, reject) => {
        const options = {
            scriptPath: path.join(__dirname, 'python'),
            args: [],
            pythonOptions: ['-u'],
        };

        const input = JSON.stringify({ method, url, headers, data });

        const shell = new PythonShell('curl_wrapper.py', options);
        shell.send(input);

        let result = '';
        shell.on('message', (message) => {
            result += message;
        });

        shell.on('close', () => {
            try {
                resolve(JSON.parse(result));
            } catch (err) {
                reject(err);
            }
        });

        shell.on('error', (err) => {
            reject(err);
        });
    });
}

module.exports = { curlRequest };
