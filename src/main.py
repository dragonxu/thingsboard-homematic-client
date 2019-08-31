import requests
import homematicip
import json
from homematicip.home import Home
from homematicip.device import Device

from thingsboard import ThingsboardConnection

def main():
    config = homematicip.find_and_load_config_file()
    home = Home()
    home.set_auth_token(config.auth_token)
    home.init(config.access_point)

    c = lambda: None
    c.__dict__ = config.raw_config['TB']
    tb = ThingsboardConnection(c)

    home.get_current_state()
    for g in home.groups:
        if g.groupType=="META":
            for d in g.devices:
                x = tb.getOrCreateDevice(g, d)  
                x.updateTelemetryFromHmIP(g, d)
                

if __name__ == "__main__":
    main()