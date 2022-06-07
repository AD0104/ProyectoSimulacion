from simpy.core import Environment
from model.simpy_config import configuracion
from model.simpy_config import get_arrival_messages, get_entry_messages, get_out_messages
from model.simpy_config import get_times, set_time_lists


def get_arriving_text()->list:
    return get_arrival_messages()

def get_entry_text()->list:
    return get_entry_messages()

def get_out_text()->list:
    return get_out_messages()
    
def set_simpy_env(form_data: dict):
    env = Environment()
    env.process(configuracion(
                    env, 
                    int(form_data['washing-stations']), 
                    form_data["simulation-day"], 
                    int(form_data['workers'])
                ))
    env.run(until=int(form_data['simulation-time']))
    get_times()
    set_time_lists()
