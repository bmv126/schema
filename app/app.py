from flask import Flask
from flask import jsonify,request
from jsonschema import validate
import json

app = Flask(__name__)

def load_schema():
    with open('schema/validSchema.json', 'r') as f:
        loadedJsonSchema = json.load(f)
    return loadedJsonSchema

def isSchemaValid(inputJson):
    jsonSchema = load_schema()
    try:
       validate(inputJson,jsonSchema)
       isValid = True
    except:
       isValid = False
    return isValid

@app.route('/api/v1/',methods=['POST','GET'])
def valididateInput():
    if request.method == 'POST':
       inputJson = request.get_json()
       if(isSchemaValid(inputJson)):
         return jsonify({'InputJson':'valid'})

       return jsonify({'InputJson':'Invalid'})
    else:
       return jsonify(load_schema())

app.run('localhost',debug=True)