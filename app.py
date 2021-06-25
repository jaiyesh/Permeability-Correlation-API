from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

@app.route('/',methods = ['GET','POST']) #To render homepage
def home_page():
    return render_template('index.html')
@app.route('/permeability',methods = ['POST'])
def perm_calculation():
    if (request.method =='POST'):
        operation = request.form['operation']
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        if(operation == "Timur Correlation"):
            r = 8.58102*(num1**4.4)/(num2**2)
            result = "The estimation of permeability by using Timur Equation is: " + str(r) + " darcy."
        if (operation == "Morris-Biggs Oil Reservoir Correlation"):
            r = 62.5 * (num1**6) / (num2**2)
            result = "The estimation of permeability by using Morris-Biggs Oil Reservoir Equation is: " + str(r) + " darcy."
        if (operation == "Morris-Biggs Gas Reservoir Correlation"):
            r = 2.5 * (num1**6) / (num2**2)
            result = "The estimation of permeability by using Morris-Biggs Gas Reservoir Correlation Equation is: " + str(r) + " darcy."

        return render_template('results.html', result = result)

if __name__ == "__main__":
    app.run(debug = True)
