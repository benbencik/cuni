#!/usr/bin/env python3

import argparse
import io
import os
from re import I
import sys

import jinja2
import roman


def jinja_filter_liters_to_gallons(text):
    return float(text) * 0.264172052

def a2r(number):
    try:
        num = int(number)
        if num <= 0: 
            os.write(2, str.encode(f"Warning: arabic2roman: unable to convert {number}."))
            return "NaN"
        return roman.toRoman(number)
    except:
        os.write(2, str.encode(f"Warning: arabic2roman: unable to convert {number}."))
        return "NaN"

def get_jinja_environment(template_dir, gallons):
    env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir),
                             autoescape=jinja2.select_autoescape(['html', 'xml']),
                             extensions=['jinja2.ext.do'])
    if gallons: env.filters['l2gal'] = jinja_filter_liters_to_gallons
    env.filters['arabic2roman'] = a2r
    return env



def main(argv):
    args = argparse.ArgumentParser(description='Templater')
    args.add_argument(
        '--template',
        dest='template',
        required=True,
        metavar='FILENAME.j2',
        help='Jinja2 template file')
    args.add_argument(
        '--input',
        dest='input',
        required=True,
        metavar='INPUT',
        help='Input filename'
    )
    args.add_argument('--use-us-gallons', action='store_true', dest='gallons')

    config = args.parse_args(argv)

    env = get_jinja_environment(os.path.dirname(config.template), 1)
    template = env.get_template(config.template)

    variables = {
        'content': "",
        'TEMPLATE': config.template,
        'INPUT': config.input,
    }

    with open(config.input, 'r') as f:
        in_header = 0
        add_to_list = [False, ""]
        while f:
            line = f.readline()
            if in_header == 2: variables['content'] += line
            line = line.strip()
            if not line: break
            
            if line == "---":
                # check if i am in header
                in_header += 1
            elif in_header:
                if add_to_list[0]:
                    # appending to the list
                    var = line.split(" ")
                    if var[0] == "-": variables[add_to_list[1]].append(var[1])
                    else: add_to_list[0] = False
                else:
                    # assign variables
                    var = line.split(":")
                    if var[1]: 
                        variables[var[0]] = var[1][1:]
                    else:
                        variables[var[0]] = []
                        add_to_list = [True, var[0]]
                    
    # Use \n even on Windows
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, newline='\n')

    result = template.render(variables)
    print(result)


def enrty_point():
    # if __name__ == '__main__':
    main(sys.argv[1:])

if __name__ == '__main__':
    main(sys.argv[1:])
