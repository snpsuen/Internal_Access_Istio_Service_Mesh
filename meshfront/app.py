from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/accessmesh', methods=['GET', 'POST'])
def accessmesh():
  if request.method == 'POST':
    path = request.form['path']
    return redirect(f"http://service-mesh/{path}")
