from tkinter import END
from simpy.core import Environment
from model.simpy_config import configuracion
from model.simpy_config import get_times, get_arrival_messages, get_entry_messages, get_out_messages
from model.simpy_config import get_times, set_time_lists
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
def set_simulation_times()->None:
    global sim_times 
    sim_times = get_times()
def get_simulation_times()->dict:
    set_simulation_times()
    return sim_times
def get_arriving_text()->list:
    return get_arrival_messages()
def get_entry_text()->list:
    return get_entry_messages()
def get_out_text()->list:
    return get_out_messages()
def set_clean_lists()->None:
    print("cleaning...")
    set_time_lists([0])
def set_simpy_env():
    env = Environment()
    general_data = get_entry_data()
    env.process(configuracion(env, general_data['stations'], general_data["simulation-day"]))
    env.run(until=general_data['simulation-time'])
    get_times()