#!/usr/bin/env python3

import argparse
import io
import os
import sys

import jinja2

def jinja_filter_liters_to_gallons(text):
    return float(text) * 0.2199692


def get_jinja_environment(template_dir):
    env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir),
                             autoescape=jinja2.select_autoescape(['html', 'xml']),
                             extensions=['jinja2.ext.do'])
    env.filters['l2gal'] = jinja_filter_liters_to_gallons
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

    config = args.parse_args(argv)

    env = get_jinja_environment(os.path.dirname(config.template))
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
