#!/usr/bin/env python3
# coding: utf-8

from slugify import slugify
import yaml
import pandas as pd
import argparse
import os

from jinja2 import Environment, FileSystemLoader

env = Environment(
    loader=FileSystemLoader('.'), lstrip_blocks=True, trim_blocks=True)

parser = argparse.ArgumentParser()

challenge_path = '../_challenges'


def input_csv(infile, transpose=True):
    """
    Open a CSV file for reading
    """
    with open(infile, newline='') as csvfile:
        df = pd.read_csv(csvfile)
    if transpose:
        df.set_index('Attribute', inplace=True)
        df = df.transpose()
    return df


def relabel_df(df):
    """
    Modify the column labels to fit into Jekyll. Default to lowercase.
    """
    df = df.rename(columns={'Title': 'title',
                            'Teaser text': 'excerpt',
                            'Description': 'description',
                            'Example projects': 'projects',
                            'Tags': 'tags',
                            'Mentors': 'mentors',
                            'Resources': 'resources',
                            'Badge': 'badge',
                            'Level': 'level'
                            })
    return df


def csv2dict(df):
    """
    Convert the dataframe created by pandas to a dict
    """
    csvdict = df.to_dict(orient='records')[0]

    try:
        tags = csvdict['tags'].split(',')
        tags = [t.strip() for t in tags]
        csvdict['tags'] = tags
    except AttributeError:
        pass

    try:
        mentors = csvdict['mentors'].split(',')
        mentors = [m.strip() for m in mentors]
        csvdict['mentors'] = mentors
    except AttributeError:
        pass
    return csvdict


def make_outfname(csvdict):
    """
    Use the title of the challenge to generate a filename for the output.
    """
    outfname = slugify(csvdict['title']) + '.md'
    outfpath = os.path.join(challenge_path, outfname)
    return outfpath


def build_content(csvdict):
    """ 
    Construct a new dictionary that will be used to populate the template.
    """
    yamlkeys = ['title', 'excerpt', 'tags', 'mentors', 'badge', 'level']
    #yamlkeys = ['title', 'excerpt', 'tags']
    yamldict = {}
    content = csvdict.copy()

    #sidekeys = ['mentors', 'badge', 'level']

    for k in yamlkeys:
        yamldict[k] = csvdict[k]
        del content[k]
    yml = yaml.dump(yamldict)
    content['yaml'] = yml
    return content


def render_template(content, outfpath, tpl='template.md', debug=False):
    """
    Render the template and write to a file.
    """
    template = env.get_template(tpl)

    t = template.render(content=content)
    with open(outfpath, 'w') as outfile:
        print(t, file=outfile)
        print('Printing to {}'.format(outfpath))
    if debug:
        print(t)


def main():
    parser.add_argument(dest='infile', type=str, nargs='+')
    args = parser.parse_args()
    for arg in args.infile:
        df = input_csv(arg)
        df = relabel_df(df)
        csvdict = csv2dict(df)
        outfpath = make_outfname(csvdict)
        content = build_content(csvdict)
        render_template(content, outfpath, debug=False)


if __name__ == "__main__":
    main()
