def generate_index_page(df, show_topcat, show_subcat):
    """
    :param df: dataframe with page meta data
    :return: list with index page content (list of html strings)
    """

    # init
    index_page_title = f"<h3 id='id_contents'>Contents</h3>"
    index_page_content = '<table style="line-height: 1.6;"><tr><td style="padding:20px; vertical-align: top;">'

    # calc for splitting index page contents into columns
    helft = max(15, int(df.shape[0] / 2))  # aantal items per html table kolom, maar tenminste 15
    derde = max(15, int(df.shape[0] / 2.7))  # aantal items per html table kolom, maar tenminste 15

    # import category descriptions (to show as tooltip infobutton)
    # cats = import_categories()

    # info button html
    ib_html = '<span title="VAR_CATEGORY" style="background: #4FB4E3; border-radius: 50%; height: 1.1em; width: 1.1em; text-align: center; color: #FFF; line-height: 1.1em; display:inline-block; font-weight: bold;">?</span>'

    # category
    for i, r in df.iterrows():

        # invoegen top category label
        if 'topcat' in df.columns and show_topcat:
            if r['topcat'] != r['next_tcat']:
                title = r['topcat']  # hier evt. nog een cat description toevoegen
                index_page_content += f"{'<br>' if i > 0 else ''}<span title='{title}' style='color: white; background-color: #008AC9; padding:5px;'>{r['topcat'].upper()}</span><br><br>"

        # ivoegen sub category label
        if 'subcat' in df.columns and show_subcat:
            if r['subcat'] != r['next_scat']:
                cat_description = ''  # cats.get(r['category'], None)  # check if category description is available
                info_button_category = ib_html.replace('VAR_CATEGORY', cat_description) if cat_description else ''
                index_page_content += f"<b>{r['subcat']}</b>&nbsp;&nbsp;{info_button_category}<br>"

        if (i + 1) % derde == 0:  # nieuwe table column
            index_page_content += f'</td><td style="padding:20px; vertical-align: top;">'

        if 'highlight' in df.columns:
            bulb = df[df.index == i].highlight.values[0]  # bullet = &#8226;
        else:
            bulb = False
        index_page_content += f"&nbsp;&nbsp;&nbsp;&nbsp;{i + 1}.&nbsp;<a href='#{r['pagekey']}'>{df[df.index == i].title.values[0]}</a> {'&#128161;' if bulb else ''}<br>"

    index_page_content += f"</td></tr></table>"

    return index_page_title + index_page_content


def generate_highlights_page(df, show_topcat, show_subcat):
    """
    :param df: dataframe with page meta data
    :return: list with highlights page content (list of html strings)
    """

    # init
    hl_page_title = f"<h3 id='highlights'>Highlights summary &#128161;</h3><span  style='line-height: 1.6;'>"
    hl_page_content = ''

    # add new line for each content page
    for i, r in df.iterrows():

        # invoegen top category label
        if 'topcat' in df.columns and show_topcat:
            if r['topcat'] != r['next_tcat']:
                hl_page_content += f"<br><span title='{r['topcat'].upper()}' style='color: white; background-color: #008AC9; padding:5px;'>{r['topcat'].upper()}</span><br><br>"

        # invoegen sub category label
        if 'subcat' in df.columns and show_subcat:
            if r['subcat'] != r['next_scat']:
                hl_page_content += f"<b>{r['subcat']}</b><br>"

        # show comments for highlighted titles
        if r['highlights']:
            for comment in r['highlights']:
                hl_page_content += f"&nbsp;&nbsp;&nbsp;&nbsp;&#8226;&nbsp;<a href='#{r['pagekey']}'>{r['title']}</a>: {comment}<br>"

    hl_page_content += '</span>'

    return hl_page_title + hl_page_content
