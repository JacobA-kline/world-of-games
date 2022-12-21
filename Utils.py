from os import system, name

SCORES_FILE_NAME = "scores.json"
BAD_RETURN_CODE = 13


def screen_cleaner():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

