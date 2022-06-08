from urllib import response
from flask import Flask, render_template, jsonify, make_response
from flask import request
from controller.middle import set_simpy_env, clear_lists
from controller.middle import get_arriving_text, get_entry_text, get_out_text, get_sim_times

app = Flask(__name__, static_folder="./static", template_folder="./templates")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get-form-data', methods=['GET', 'POST'])
def get_simulation_config_parameters():
    clear_lists()
    form_data = request.get_json()
    set_simpy_env(form_data=form_data)
    messages = {
        "arrivals": get_arriving_text(),
        "entrys": get_entry_text(),
        "outs": get_out_text()
    }
    average_times = get_sim_times()
    messages.update(average_times)
    print(messages)
    response = make_response(
        jsonify(
            messages
        )
    )
    return response
