from flask import Flask, url_for, request, json, Response, jsonify

data = None
app = Flask(__name__)

@app.route('/')
def api_root():
    """Home page method"""
    return 'Home page' #return render_template('index.html')

@app.route('/info', methods = ['GET'])
def api_info():
    """Method informing about project progress. To check results: curl -i http://127.0.0.1:5000/info"""
    data = {
        'Version'  : '0.2',
        'License' : '',
        'Authors ': ['Szymon Janowski', 'Agnieszka Rusin', 'Bartosz Mikulski']
    }
    js = json.dumps(data)
    resp = Response(js, status=200, mimetype='application/json')
    resp.headers['Link'] = '?domain_name'
    return resp

#-------------------- curl helper --------------------

@app.route('/echo', methods = ['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
def api_echo():
    if request.method == 'GET':
        return "ECHO: GET\n"

    elif request.method == 'POST':
        return "ECHO: POST\n"

    elif request.method == 'PATCH':
        return "ECHO: PACTH\n"

    elif request.method == 'PUT':
        return "ECHO: PUT\n"

    elif request.method == 'DELETE':
        return "ECHO: DELETE"

#-----------------------------------------------------

@app.route('/do', methods = ['POST'])
def api_do():
    """Processing JSON file. To check how it works: curl -X POST http://127.0.0.1:5000/do --data @nazwa_jsona.json"""
    global data
    data = request.get_json(force=True)
    js = json.dumps(data)
    #modify JSON here
    print(js)
    return jsonify(js)

#-----------------------------------------------------

@app.errorhandler(404)
def not_found(error=None):
    message = {
            'status': 404,
            'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404
    return resp

#-----------------------------------------------------

if __name__ == '__main__':
    app.run()