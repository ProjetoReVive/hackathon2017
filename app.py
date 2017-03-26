import re
import json
from flask import Flask, render_template, url_for
from flask import request, Response
from flask import json, jsonify


app = Flask(__name__)
	
@app.route("/")
def form():
	return render_template('form_submit.html')


@app.route('/login/', methods=['POST'])
def login():
	
	# Lendo query string
	user=request.form['user']
	pass=request.form['pass']
	
	# Adaptando para json 
	user_account = jsonify(request.form)

	# Obtendo contas registradas
	with open('db/accounts.json') as data_file:    
    	account_list = json.load(data_file)

	for account in account list
	# Validando valores 	
	#if (not re.match("^[A-Za-z]*$", unsafe_name)
	#		or not re.match(r'[\w.-]+@[\w.-]+', unsafe_email)):
	#	return render_template('form_fail.html') 
	#else:
	#	name = unsafe_name
	#	email = unsafe_email
	return jsonify(request.form)#render_template('form_action.html', name=name, email=email) + jsonify(request.form)


@app.route('/json', methods = ['GET'])
def api_json():
    data = {
        'hello'  : 'world',
        'number' : 3
    }
    js = json.dumps(data)

    resp = Response(js, status=200, mimetype='application/json')
    #resp.headers['Link'] = 'http://luisrei.com'

    return resp


if __name__ == "__main__":
	app.run()
