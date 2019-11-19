#!ENV/bin/python3

import os

def get_env_var (env_var_name):
    try:
        env_var = os.environ[env_var_name]
    except KeyError:
        print (__file__+': error: '+env_var_name+" environment variable does not exist!")
        sys.exit(1)
    return env_var
