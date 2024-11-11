from flask import Flask, send_file, request

app = Flask(__name__)

@app.route('/get/firmware')
def api_firmware_data():
    try:
        return send_file('fw1_to_fw2.bin')
    except Exception as e:
        return str(e)


@app.route('/')
def hello_word():
    return "<p>Esp32 OTA Server running on: " + request.host + " !</p>"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9001, debug=True, threaded=True)