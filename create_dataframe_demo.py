import numpy as np
import pandas as pd


def custom_blues(value):
    if value < 0 or value > 1:
        raise ValueError("Value must be between 0 and 1.")

    start_color = (255, 255, 255)  # white
    end_color = (89, 99, 235)  # darkest blue in the original Blues colormap

    r = start_color[0] + value * (end_color[0] - start_color[0])
    g = start_color[1] + value * (end_color[1] - start_color[1])
    b = start_color[2] + value * (end_color[2] - start_color[2])

    return r / 255, g / 255, b / 255


def demo_df_html():
    # create dummy data
    data = np.random.rand(10, 5)
    df = pd.DataFrame(data, columns=['column1', 'column2', 'column3', 'column4', 'column5'],
                      index=['row1', 'row2', 'row3', 'row4', 'row5', 'row6', 'row7', 'row8', 'row9', 'row10'])

    # style dataframe
    formatted_df = df.style.format("{:,.0%}")
    styled_df = (formatted_df
                 .set_table_styles([{'selector': 'th', 'props': [('font-weight', 'bold')]}])
                 .set_table_styles([{'selector': 'th', 'props': [('padding', '3px 10px 3px 10px')]}])
                 .set_properties(**{'padding': '3px 10px 3px 10px'})
                 .set_properties(**{'margin': '3px'})
                 .set_properties(**{'text-align': 'right'}))

    # add blues colormap
    def apply_custom_blues(val):
        norm_val = (val - df.values.min()) / (df.values.max() - df.values.min())
        color = custom_blues(norm_val)
        return f'background-color: rgba({color[0] * 255:.0f}, {color[1] * 255:.0f}, {color[2] * 255:.0f}, 1)'

    styled_df = styled_df.applymap(apply_custom_blues)

    # Find the row and column with the highest value
    max_value = df.max().max()
    max_location = np.where(df == max_value)
    max_row = df.index[max_location[0][0]]
    max_col = df.columns[max_location[1][0]]

    # Find the row and column with the lowest value
    min_value = df.min().min()
    min_location = np.where(df == min_value)
    min_row = df.index[min_location[0][0]]
    min_col = df.columns[min_location[1][0]]

    # apply highlights in df
    styled_df.applymap(lambda x: 'border: 5px solid red', subset=pd.IndexSlice[max_row, max_col])
    styled_df.applymap(lambda x: 'border: 5px solid green', subset=pd.IndexSlice[min_row, min_col])

    return styled_df.to_html()


folium_html = demo_df_html()
with open(r'webslides/modules/df_demo.html', 'w') as f:
    f.write(folium_html)
print('df_demo.html saved to file')
