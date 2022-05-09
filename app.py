from flask import Flask,request,jsonify
from flask_cors import CORS
import Invoice_ML
app = Flask(__name__)
CORS(app) 
@app.route('/predict', methods=['GET'])
def recommend_movies():
        res = Invoice_ML.getdate(request.args.get('number'),float(request.args.get('amt')))
        print(request.args.get('number'),request.args.get('amt'))
        return jsonify(res)

if __name__=='__main__':
        app.run(port = 5000, debug = True)