#!/usr/local/bin/env python3
# coding: utf-8

import os

from jinja2 import Environment, FileSystemLoader

env = Environment(
    loader=FileSystemLoader('.'),lstrip_blocks=True, trim_blocks=True)
import argparse

import pandas as pd
import yaml
from slugify import slugify

parser = argparse.ArgumentParser()

challenge_path = '../_challenges'

def input_csv(infile):
    with open(infile, newline='') as csvfile:
        df = pd.read_csv(csvfile)
    return df

def relabel_df(df):
    df = df.rename(columns={'Title':'title',
                            'Teaser text':'excerpt',
                            'Description':'description', 
                            'Example projects':'projects',
                            'Tags':'tags',
                            'Mentors':'mentors',
                            'Resources':'resources',
                            'Badge':'badge',
                            'Level':'level'
                           })
    return df


def csv2dict(df):
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
    outfname = slugify(csvdict['title']) + '.md'
    outfpath = os.path.join(challenge_path, outfname)
    return outfpath

def build_content(csvdict):
    yamlkeys = ['title', 'excerpt', 'tags', 'mentors', 'badge', 'level']
    #yamlkeys = ['title', 'excerpt', 'tags']
    yamldict = {}
    content = csvdict.copy()

    #sidekeys = ['mentors', 'badge', 'level']

    for k in yamlkeys:
        yamldict[k]= csvdict[k]
        del content[k]
    yml = yaml.dump(yamldict)
    content['yaml'] = yml
    return content

def render_template(content, outfpath, tpl = 'template.md', debug = False):
    template = env.get_template(tpl)

    t = template.render(content=content)
    with open(outfpath, 'w') as outfile:
        print(t, file=outfile)
        print('Printing to {}'.format(outfpath))
    if debug:
        print(t)


def main():
    df = input_csv('tp1.csv')   
    df = relabel_df(df)
    csvdict = csv2dict(df)
    outfpath = make_outfname(csvdict)
    content = build_content(csvdict)
    render_template(content, outfpath, debug=False)


if __name__ == "__main__":
    main()


