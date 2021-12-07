
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
	return 'Ini adalah halaman depan'

@app.route('/a')
def a():
  return render_template('template.html')
  
if __name__ == '__main__':
  app.run()
