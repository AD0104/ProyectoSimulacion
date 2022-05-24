from tkinter import END
from simpy.core import Environment
from  simpy_config import configuracion
from simpy_config import get_times, get_arrival_messages, get_entry_messages, get_out_messages
def set_entry_data(root):
    global data_dict
    data_dict = {
        "stations": root.get_washing_stations(),
        "simulation-time": root.get_simulation_time(),
        "simulation-day": root.get_simulation_day()
    }
    set_simpy_env()
def get_entry_data()->dict:
    return data_dict
def set_simulation_times(times: dict)->None:
    global sim_times 
    sim_times = times
def get_simulation_times()->dict:
    return sim_times
def get_arriving_text()->list:
    return get_arrival_messages()
def get_entry_text()->list:
    return get_entry_messages()
def get_out_text()->list:
    return get_out_messages()
def set_simpy_env():
    env = Environment()
    general_data = get_entry_data()
    env.process(configuracion(env, general_data['stations'], general_data["simulation-day"]))
    env.run(until=general_data['simulation-time'])
    get_times()
