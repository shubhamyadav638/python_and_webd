from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('demo.html')
    

@app.route('/get-data', methods=['POST'])
def mydata():
   
    data=request.form
    first_name = data["first_name"]
    last_name = data["last_name"]
    mydata="first_name : "+first_name+' last_name: '+ last_name 
    return mydata
if __name__=="__main__":
    app.run(debug=True,port=8000)