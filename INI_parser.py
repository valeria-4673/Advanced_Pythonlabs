import configparser

config = configparser.ConfigParser()
print(config.read('mess.ini'))
print('Sections:', config.sections(),'\n')


sections_dev = {}
sections_prod = {}


for section in config.sections():
    if config[section]["env"] == "dev":
        para_dict= ""
        for key in config[section]:
            value = config[section][key]
            if value == "dev":
                continue
            para_dict += f"{key} = {value}"
        sections_dev[section] = para_dict
        
print("Sections dev: ", sections_dev)
