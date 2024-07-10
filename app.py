from flask import Flask, render_template, jsonify, request
from game import initialize_grid, update_grid

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/initialize')
def initialize():
    grid = initialize_grid()
    return jsonify(grid)

@app.route('/update', methods=['POST'])
def update():
    grid = request.json['grid']
    next_grid = update_grid(grid)
    return jsonify(next_grid)

if __name__ == '__main__':
    app.run(debug=True)