import os, sys
from dotenv import load_dotenv

load_dotenv()
env_vars = os.environ

def list_writer(text_list, *args, **kwargs):
    string_path = env_vars["DESKTOP_PATH"]
    file_path = os.path.expanduser(string_path)

    with open(file_path, "w", encoding='utf-8') as file:
        file.write("\n".join(text_list))
