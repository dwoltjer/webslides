import os
import numpy as np
import pandas as pd
import plotly.express as px

from webslides.main import create
from .other import hello_world_html, code_to_html


def demo_plotly_fig():
    # Load the iris dataset provided by the library
    df = px.data.iris()
    fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species",
                     size='petal_length', hover_data=['petal_width'],
                     title="Iris Dataset: Sepal Dimensions and Petal Characteristics by Species")
    fig.update_layout(height=700)
    return fig


def demo_folium_html():
    fname = 'folium_demo.html'
    current_dir = os.path.dirname(os.path.abspath(__file__))
    fpath = os.path.join(current_dir, fname)
    with open(fpath, 'r') as f:
        demo_html = f.read()
    return demo_html


def demo_df_html():
    fname = 'df_demo.html'
    current_dir = os.path.dirname(os.path.abspath(__file__))
    fpath = os.path.join(current_dir, fname)
    with open(fpath, 'r') as f:
        df_html = f.read()
    return df_html


def demo():
    """Creates documentation explaining why and how to use this package"""

    title_page = {
        'img_url': '',
        'title': 'Webslides Documentation',
        'summary': {
            'About': 'Webslides is a Python package that creates HTML presentations <b>like this one</b>.<br>It enables easy sharing of Python-generated content such as charts, other visuals and data',
            'Contents': 'This presentation demonstrates features of the HTML format and should help you get started',
            'PyPi': '<a href="https://pypi.org/project/webslides/">https://pypi.org/project/webslides/</a>'}
    }

    content = {
        'WHY': {'Advantages over Powerpoint':
                    [{'title': 'Dynamic pagelength',
                      'highlights': ['- Pages can be as long (or short) as needed, like this one!'],
                      'body': 'Nothing much on this page really, that\'s why its so short 😉',
                      'footer': ['- and adding a footer can be usefull too..',
                                 '- ps. Have you noted the page navigation on the top right of the page?',
                                 '- &#x1F4A1;: this marks pages with a highlight. If a page has no highlights (remarks in grey area) it is not shown in the highlight summary page nor marked in the table of contents']},
                     {'title': 'Interactive content',
                      'highlights': [
                          '- Native Plotly graph ojects can be inserted as content, and they have many interactive features',
                          '- Try zooming in the by dragging a window in the plot. Or toggle visibility of a data series via the legend keys'],
                      'body': demo_plotly_fig(),
                      'footer': ['- Link to Plotly gallery <a href="https://plotly.com/python/">here</a>']},
                     {'title': 'Any HTML content will render',
                      'highlights': ['- For example this map'],
                      'body': demo_folium_html(),
                      'footer': [
                          '- this map was created with Folium (<a href="https://python-visualization.github.io/folium/">docs</a>)']},
                     {'title': 'Styled Pandas Dataframes',
                      'highlights': ['- Wow, notice that max value marked red',
                                     '- Not to mention the lowest value, marked green'],
                      'body': demo_df_html(),
                      'footer': [
                          '- styling of a pandas dataframe can be done by creating a styler object and convert that to html',
                          '- ie. styled_df = df.style.background_gradient(cmap=\'Blues\') and html = styled_df.to_html()']},
                     {'title': 'Super speed updates!',
                      'highlights': [
                          '- A key advantage of this presentation form may be that updates only require the <i>press of a button</i>'],
                      'body': 'Very often data, analysis conlusions and other content is revised in getting to a final version of a presentation. Since all is in python script, updates of the presentation only requires the press of the ▶ Run button.',
                      'footer': ['- and pagination will automatically adjust if new content is inserted']
                      }
                     ]
                },
        'HOW': {'Getting Started': [{
            'title': 'Install and Import',
            'highlights': ['- Nothing new here, good old pip install..'],
            'body': code_to_html(
                '#install package<br>pip install webslides<br><br>#import package<br>import webslides as ws')},
            {'title': 'Run Demo',
             'highlights': ['- ws.demo() will generate the html you are reading now'],
             'body': code_to_html(
                 '#import<br>import webslides as ws<br><br>#create and open this demo.html in browser<br>ws.demo()'),
             'footer': [
                 '- html output file, in this case \'demo.html\', is always saved to a directory \'wsout\'']},
            {'title': 'Hello World',
             'highlights': ['- basic example, demonstrating all available parameters'],
             'body': hello_world_html(),
             'footer': [
                 '- HTML allows to add javascript too, like the copy button. That\'s actually only one line of code']}
        ]
        }}

    create(content=content
           , title_page=title_page
           , fname='demo.html'
           , show_topcat=True
           , show_subcat=True
           , open_in_browser=True
           , show_index_page=True
           , show_highlights_page=True
           , show_highlights_only=False)

    return None

demo()