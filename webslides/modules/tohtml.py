import datetime as dt
import plotly.offline as po


def titlepage_to_html(html, page):
    # check if image is provided, otherwise swap for Webslides logo HTML
    if ('img_url' in page) and len(page['img_url']) > 0:

        # image url was provided
        VAR_IMAGE_HTML = "<img src='" + page['img_url'] + "' style='width:200px;margin:10px;'>"

    else:

        # no image url provided
        VAR_IMAGE_HTML = ws_logo_html()

    # init
    titlepage = """<style>
    .container {position: relative; height: 600px;}
    .centered-element {text-align: center; margin: 0; width:80%; position: absolute; top: 50%; left: 50%; -ms-transform: translate(-50%, -50%); transform: translate(-50%, -50%);}
    </style>
    <div class='container'>
        <div class='centered-element'>
            VAR_IMAGE_HTML
            <h1>VAR_TITLE</h1><br>
            <p style='line-height: 1.5;'>
            VAR_SUMMARY</p>
        </div>
    </div>"""

    titlepage = titlepage.replace('VAR_IMAGE_HTML', VAR_IMAGE_HTML)
    titlepage = titlepage.replace('VAR_TITLE', page['title'])

    # generate summary html
    summary_html = """
        <table style="width: 100%; text-align: left; font-size: 1em; border-collapse: collapse; border: 0;">
            <colgroup>
                <col style="width: 20%;">
                <col style="width: 80%;">
            </colgroup>
            <tbody>"""

    for k, v in page['summary'].items():
        summary_html += f"""
                <tr style="border: 0;">
                    <td style="border: 0; padding: 10px; text-decoration: underline; vertical-align: top; text-align: right;">{k}</td>
                    <td style="border: 0; padding: 10px;">{v}</td>
                </tr>
                """
    summary_html += """
                <!-- more rows here -->
            </tbody>
        </table>"""

    titlepage = titlepage.replace('VAR_SUMMARY', summary_html)

    html = html.replace('<span></span>', titlepage + '<span></span>')

    # footer
    if 'footer' in page:
        footer = page['footer']
        footer.append(f"{dt.datetime.now().strftime('%e %b. %Y')}")
        footer_html = footer_to_html(page['footer'])
        html = html.replace('<span></span>', footer_html + '<span></span>')

    return html


def content_to_html(html, page, show_topcat, show_subcat, show_index_page=False, show_highlights_page=False,
                    show_navi=False):
    # A. page navigation
    if show_navi:  # dont show for title page
        pagenavi = pagenavi_to_html(pageno=page['pageno'],
                                    pagekey=page['pagekey'],
                                    show_index_page=show_index_page,
                                    show_highlights_page=show_highlights_page,
                                    prev_highlight_key=page.get('hl_prev_key', None),
                                    next_highlight_key=page.get('hl_next_key', None))
        html = html.replace('<span></span>', pagenavi + '<span></span>')

    # B. page title
    if 'title' in page and page['title'] != '':
        title = title_to_html(page['topcat'], page['subcat'], page['title'], show_topcat, show_subcat)
        html = html.replace('<span></span>', title + '<span></span>')

    # C. highlights
    if 'highlights' in page and page['highlights'] != '':
        highlights_html = highlights_to_html(page['highlights'])
        html = html.replace('<span></span>', highlights_html + '<span></span>')

    # D. body
    if 'body' in page:
        body_html = body_to_html(page['body'])
        html = html.replace('<span></span>', body_html + '<span></span>')

    # E. footer
    if 'footer' in page and page['footer'] != '':
        footer_html = footer_to_html(page['footer'])
        html = html.replace('<span></span>', footer_html + '<span></span>')

    return html


def pagenavi_to_html(pageno, show_index_page, show_highlights_page, pagekey, prev_highlight_key, next_highlight_key):
    """
    :param pageno: int pagenumber
    :param name: str name of the html page (id used to navigate to this page, ie. from index page)
    :param show_index_page: bool if False, references to index page are omitted
    :param show_highlights_page: bool if False, references to highlights page are omitted
    :param prev_highlight_key: str html id of previous highlight page
    :param next_highlight_key: str html id of next highlight page
    :return: string html code to place on top of each page, used for
        - navigation to next/previous highlight page
        - navigation to index page
        - navigation to highlights page
        - display pagenumber
        - page id tag used to navigate to that page
    """

    link_prev = '' if prev_highlight_key == '' else f'<a title="Previous highlight" href="#{prev_highlight_key}">&#9664;</a>'
    link_next = '' if next_highlight_key == '' else f'<a title="Next highlight" href="#{next_highlight_key}">&#9658;</a>'

    pagenavi_index_page = f'<a id="{pagekey}" title="Table of contents" href="#id_contents">&#128196;</a> ' * show_index_page
    pagenavi_highlights_page = f'{link_prev} <a title="Highlights summary" href="#highlights">&#128161;</a> {link_next} ' * show_highlights_page

    pagenavi_html = f'<div class="footer" style="width: 100%; margin: 0 auto; text-align:right;">{pagenavi_highlights_page}{pagenavi_index_page}p{pageno}</div>'

    return pagenavi_html


def title_to_html(topcat='', subcat='', title='', show_topcat=True, show_subcat=True):
    """
    :param title: str title of html page
    :return: string html formatted title
    """
    topcat = f"<span style='color: white; background-color: #008AC9; padding:5px;'>{topcat.upper()}</span> " if len(
        topcat) > 0 else ''
    subcat = f"<span style='font-weight: normal;'>{subcat}</span>: " if len(subcat) > 0 else ''
    return f"<h3 style='line-height: 2;'>{show_topcat * topcat}{show_subcat * subcat}{title}</h3>"


def highlights_to_html(highlights):
    """
    :param comments: list with text to show in header
    :return: string html formatted header
    """
    html = '<div style="background-color: #EBEBEB; line-height: 1.6; padding:10px;">'
    for o in highlights: html += f"{o}<br>"
    html += "</div>"
    return html


def body_to_html(body):
    # insert html string
    if isinstance(body, str):
        # add some padding to the body content
        return f"<div style='padding:3%'>{body}</div>"

    # if not string, must be plotly fig object
    else:
        return f"<div style='padding:3%'>{po.plot(body, include_plotlyjs=False, output_type='div')}</div>"


def footer_to_html(footer):
    """
    :param footer: list with text to show in footer
    :return: string html formatted footer
    """
    html = '<div style="background-color: #FFFFFF; line-height: 1.6; padding:10px;"><HR style="width:20%; margin-left:0;">'
    for o in footer: html += f"{o}<br>"
    html += "</div>"
    return html


def ws_logo_html():
    return """
        <style>
        .badge {
            width: 210px;
            height: 130px;
            margin: 42px auto;
            background: linear-gradient(to bottom right, white, #006fff);
            border: 3px solid #8ca5ff;
            border-radius: 10px;
            box-shadow: 2px 2px 5px rgb(0 0 0 / 30%);
            display: flex;
            justify-content: center;
            align-items: center;
            font-weight: bold;
            font-size: 60;
            color: #ededed;
        }
        </style>
        <div class="badge">
            <span>WS</span>
        </div>
    """
