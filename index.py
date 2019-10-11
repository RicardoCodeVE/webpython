from flask import Flask , render_template # import the module flask

app = Flask(__name__)   # create an instance named app to access to some methods like routes etc

@app.route('/')      #this way is to create routes on flask, followed a def to creeate a functioreturn the page
def home() :
    return render_template('home.html') # using the method render template it return a html page


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/career')
def career():
    return render_template('career.html')

if __name__  == '__main__':  # check if the attribute name is same to the main page 
    app.run(debug=True)  # initialize the server with the method run (), and debug =true allows reload the page when it changes
