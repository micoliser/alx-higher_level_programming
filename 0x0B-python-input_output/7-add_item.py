#!/usr/bin/python3
"""
    This module contains a script that adds all of its argument to a list and
    saves them as a JSON object in a file add_item.json
"""


def main():
    import sys
    save = __import__("5-save_to_json_file").save_to_json_file
    load = __import__("6-load_from_json_file").load_from_json_file

    file_name = "add_item.json"

    with open(file_name, "r", encoding="UTF-8") as f:
        if f.read() == "":
            arg_list = []
        else:
            arg_list = load(file_name)

    for i in range(1, len(sys.argv)):
        arg_list.append(sys.argv[i])

    save(arg_list, file_name)


if __name__ == "__main__":
    main()
