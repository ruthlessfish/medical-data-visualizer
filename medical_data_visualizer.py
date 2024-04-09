import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('medical_examination.csv')

# 2
df['overweight'] = (df['weight'] / (df['height'] / 100) ** 2) > 25
df['overweight'] = df['overweight'].astype(int)

# 3

def normalize(value):
    if value == 1:
        return 0
    elif value > 1:
        return 1
    return value

df[['cholesterol', 'gluc']] = df[['cholesterol', 'gluc']].applymap(normalize)

# 4
def draw_cat_plot():
    # 5
    df_cat = pd.melt(df, id_vars=['cardio'],
                         value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'],
                         var_name='Feature',
                         value_name='Value')


    # 6
    df_cat.groupby(['cardio', 'variable', 'Value'])['Value'].size().reset_index(name='Count')


    # 7
    g = sns.catplot(x='Feature', y='Count', hue='Value', col='cardio', data=df_cat, kind='bar', height=4, aspect=1.5)

    # 8
    fig = g.fig


    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
<<<<<<< HEAD
    # 11
    df_heat = None

    # 12
    corr = None

    # 13
    mask = None



    # 14
    fig, ax = None

    # 15



    # 16
    fig.savefig('heatmap.png')
    return fix
