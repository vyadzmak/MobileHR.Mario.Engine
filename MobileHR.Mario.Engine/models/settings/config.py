import os, sys
import modules.logging.logging as logging_config
import json
import logging

# root dir
root_dir = os.path.dirname(os.path.realpath(sys.argv[0]))

#logs dir full path
logs_dir_full_path =""

#logs dir name
logs_dir_name ="logs"

#logs dir full path
configs_dir_full_path =""

#logs dir name
configs_dir_name ="configs"

# engine version code
version_code = "0.1"

#build version code
build_version_code =-1

# engine name
engine_name = "Mario Engine"

# system name
system_name = "MobileHR Mario Engine"

# show all info when running
show_system_info_on_start = False

#logging config file name
logging_config_file_name = "logging.yaml"

#logging config file full pat
logging_config_file_full_path = ""


#buildcode file name
build_code_file_name = "build_code.json"

#logging config file full pat
build_code_file_full_path = ""

# all versions
versions_container = [
    ["0.1", "Buzzy Beetle"],
    ["0.2", "Little Goomba"],
    ["0.3", "Koopa Paratroopa"],
    ["0.4", "Koopa Troopa"],
    ["0.5", "Podoboo"],
    ["0.6", "Bullet Bill"],
    ["0.7", "Fire-Bar"],
    ["0.8", "Lakitu"],
    ["0.9", "Hammer Brother"],
    ["1.0", "Spiny's egg"],
    ["1.1", "Piranha Plant"],
    ["1.2", "Spiny"],
    ["1.3", "Turtle Cannon"],
    ["Alpha", "Cheep-cheep"],
    ["Beta", "Bloober"],
    ["RC", "Fake Bowser"],
    ["Release", "Bowser"]
]


# --------------- methods---------------#
#load and increase build version
def load_build_version():
    try:

        with open(build_code_file_full_path) as f:
            data = json.load(f)
            global build_version_code
            build_version_code= int(data["build_version_code"])
            build_version_code+=1
            data["build_version_code"] = build_version_code

        with open(build_code_file_full_path, "w") as jsonFile:
            json.dump(data, jsonFile)
            t=0
        pass
    except Exception as e:
        pass

def get_version_name():
    try:
        versions = versions_container
        current_version_code = version_code

        for version in versions:
            if (version[0] == current_version_code):
                return version[1]

        pass
    except Exception as e:
        return str(e)
        pass

#join system paths
def join_path(paths):
    try:
        path = os.path.join(*paths)
        path =os.path.normpath(path)
        # path =os.path.normcase(path)
        return path
    except Exception as e:
        return str(e)


# show start info
def show_system_info():
    try:
        print("Start init configuration")
        print("Root dir : "+root_dir)
        print("System name : "+system_name)
        print("Engine name : "+engine_name)
        print("Engine version code: "+version_code)
        print("Engine version name: "+get_version_name())
        print("Build version code: "+str(build_version_code))


        pass
    except Exception as e:
        pass

#config system paths
def config_paths():
    try:
        global configs_dir_full_path
        configs_dir_full_path = join_path([root_dir,configs_dir_name])

        global logging_config_file_full_path
        logging_config_file_full_path =join_path([configs_dir_full_path,logging_config_file_name])

        global build_code_file_full_path
        build_code_file_full_path = join_path([configs_dir_full_path,build_code_file_name])

        global logs_dir_full_path
        logs_dir_full_path = join_path([root_dir,logs_dir_name])

        t=0
        pass
    except Exception as e:
        pass

# init config
def init_config():
    try:
        config_paths()
        load_build_version()
        logging_config.setup_logging(default_path=logging_config_file_full_path)


        if (show_system_info_on_start == True):
            show_system_info()

        logging.info("Config init successful")

    except Exception as e:
        logging.error(str(e))
        pass
