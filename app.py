from flask import Flask,render_template,request,redirect,url_for
app=Flask(__name__)

@app.route("/",methods=['GET'])
def welcome():
    return "Welcome to the Flask application!"

@app.route("/index",methods=['GET'])
def index(): 
    return "Welcome to the Index!"

@app.route("/success/<score>",methods={'GET'})
def success(score):
        return "Success! Your score is: " +score
    
    
@app.route("/failure/<int:score>",methods=['GET'])
def failure(score):
        return "Failure! Your score is: " +str(score)
    
    
@app.route("/form",methods=["GET","POST"])
def form():
    if request.method == "GET":
        return render_template('form.html')
    else:
        maths=float(request.form['maths'])
        science=float(request.form['science'])
        history=float(request.form['history'])
        
    average_marks =(maths+science+history)/3
    
    if average_marks >= 50:
        return redirect(url_for('success', score=average_marks))
    else:
        return redirect(url_for('failure', score=average_marks))
    
    return render_template("form.html", score=average_marks)
        
        
if __name__ == "__main__":
    app.run(debug=True)