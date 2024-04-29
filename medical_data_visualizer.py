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
                         var_name='variable',
                         value_name='value')


    # 6
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')


    # 7
    fig = sns.catplot(x='variable', y='total', hue='value', col='cardio', data=df_cat, kind='bar')

    # 8
    fig = fig.fig


    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
        # Clean the data
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))]

    # Calculate the correlation matrix
    corr = df_heat.corr(method='pearson')

    # Generate a mask for the upper triangle
    mask = np.triu(corr)

    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(12, 12))

    # Draw the heatmap with 'sns.heatmap()'
    sns.heatmap(corr, linewidths=1, annot=True, square=True, fmt='.1f',
                mask=mask, center=0.08, cbar_kws={'shrink': 0.5})

    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
