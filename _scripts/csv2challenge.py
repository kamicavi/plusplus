#!/usr/local/bin/env python3
# coding: utf-8

from jinja2 import Environment, FileSystemLoader
env = Environment(
    loader=FileSystemLoader('.'),lstrip_blocks=True, trim_blocks=True)
import pandas as pd
import yaml
from slugify import slugify

def input_csv(infile):
    with open(infile, newline='') as csvfile:
        df = pd.read_csv(csvfile)
    return df

df = input_csv('tp3.csv')

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
df = relabel_df(df)

def csv2dict(df):
    csvdict = df.to_dict(orient='records')[0]
    outfname = slugify(csvdict['title']) + '.md'

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
    return (csvdict, outfname)

csvdict, outfname = csv2dict(df)

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

content = build_content(csvdict)

def render_template(tpl = 'template.md', debug = False):
    template = env.get_template(tpl)

    t = template.render(content=content)
    with open(outfname, 'w') as outfile:
        print(t, file=outfile)
        print('Printing to {}'.format(outfname))
    if debug:
        print(t)

render_template(debug=False)




