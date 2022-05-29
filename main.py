from flask import Flask, render_template
from flask import request

app = Flask(__name__, static_folder="./static", template_folder="./templates")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get-form-data', methods=['POST'])
def get_simulation_config_parameters():
    print(request.form)
    print(f"Washing Stations: {request.form['washing-stations']}")
    # washing_stations = request.form['washing-stations']
    # simulation_time = request.form.get('simulation-time')
    # simulation_day = request.form.get('simulation-day')
    # print(f"{washing_stations}\n{simulation_time}\n{simulation_day}")
    return index()
