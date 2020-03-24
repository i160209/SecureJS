from flask import Flask, render_template, request, jsonify

# from flask.ext.session import Session

app = Flask(__name__, static_url_path='/static')

@app.route("/")
def index():
    return render_template("SECUREJS/index.html")

@app.route("/about")
def about():
    return render_template('SECUREJS/about.html')	

@app.route("/contact")
def contact():
    return render_template('SECUREJS/contact.html')	
	
if __name__ == '__main__':
#     app.run(ssl_context='adhoc')
    app.run(debug = True)
