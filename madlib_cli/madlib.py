def welcome_message():
    print("Welcome to the Mad World of Madlibs!")
    print("Please enter various words which will be used to fill out a story template.")

def read_template(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read().strip()
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")

import re

def parse_template(model):
    parts = tuple(re.findall(r"\{(.*?)\}", model))
    stripped_model = re.sub(r"\{.*?\}", "{}", model)
    return stripped_model, parts


def merge(story_base, words):
    return story_base.format(*words)