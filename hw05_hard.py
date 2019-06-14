import sys
from hw05_easy import *

do = {
    "help": print_help,
    "mkdir": create,
    "ping": ping,
    "cp": copy_file,
    "pwd": full_path,
    "ls": files,
    "rm": delete,
    "cd": change_dir
}

name = sys.argv[2] if len(sys.argv) > 2 else None
key = sys.argv[1] if len(sys.argv) > 1 else None

do.get(key, print_help)(name)