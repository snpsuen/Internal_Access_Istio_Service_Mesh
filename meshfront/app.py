from flask import Flask, render_template, request, urllib.request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/accessmesh', methods=['GET', 'POST'])
def accessmesh():
  if request.method == 'POST':
    path = request.form['path']
    with urllib.request.urlopen(f"http://service-mesh/{path}") as response:
      contents = response.read()
    print(contents)
