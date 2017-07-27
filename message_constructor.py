import os
import random


def build_message(name=None, body=None, compliment=None):
    message = ''
    message += name if name else generate_part('names.txt')
    message += ", "
    message += body if body else generate_part('bodies.txt')
    message += " "
    message += compliment if compliment else generate_part('compliments.txt')
    message += "!"
    return message


def get_dictionary(path):
    file = open(path, 'r', encoding='utf8')
    file_contents = file.read()
    file.close()
    return file_contents.split('\n')


def generate_part(dictionary):
    path = os.path.dirname(os.path.realpath(__file__))
    path = os.path.join(path, 'dict', dictionary)
    pieces = get_dictionary(path)
    return pieces[random.randint(0, len(pieces))-1]
