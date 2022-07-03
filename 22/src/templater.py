#!/usr/bin/env python3

import argparse
import io
from itertools import accumulate
import os
import sys

import jinja2
import roman

def jinja_filter_liters_to_gallons(text):
    return float(text) * 0.2199692


def get_jinja_environment(template_dir, gallons):
    env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir),
                             autoescape=jinja2.select_autoescape(['html', 'xml']),
                             extensions=['jinja2.ext.do'])
    if gallons: env.filters['l2gal'] = jinja_filter_liters_to_gallons
    return env

def arabic2roman(number):
    if number <= 0: 
        os.write(2, "unsuccessful conversion")
        return "NaN"
    else: return roman.toRoman(number)


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

    env = get_jinja_environment(os.path.dirname(config.template), args.gallons)
    template = env.get_template(config.template)

    content = ""
    with open(config.input, 'r') as f:
        content = f.read()

    # TODO: extract YAML header next to these variables
    variables = {
        'content': content,
        'TEMPLATE': config.template,
        'INPUT': config.input,
    }

    # Use \n even on Windows
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, newline='\n')

    result = template.render(variables)

    print(result)


if __name__ == '__main__':
    main(sys.argv[1:])
