import plotly.graph_objects as go


def validate_title_page(title_page):
    if not isinstance(title_page, dict):
        return "The title page must be a dictionary"
    elif 'title' not in title_page or not isinstance(title_page['title'], str):
        return "The title page must contain a 'title' key with a string value"
    elif 'img_url' in title_page and not isinstance(title_page['img_url'], str):
        return "The image url, if provided, must be string value"
    elif 'summary' in title_page and not isinstance(title_page['summary'], dict):
        return "The summary, if provided, must be dictionary"
    elif 'footer' in title_page and not isinstance(title_page['footer'], list):
        for footer_item in title_page['footer']:
            if not isinstance(footer_item, str):
                return "Each element of the 'footer' list, if present, must be a string"
    else:
        return None


def validate_content(content):
    if not isinstance(content, dict):
        return "Error: Input is not a dictionary."

    if len(content) < 1:
        return "Error: Dictionary must have at least 1 key-value pair."

    for topcat, subcats in content.items():
        if not isinstance(subcats, dict):
            return f"Error: '{topcat}' value is not a dictionary. Content: {str(subcats)[:13]}...{str(subcats)[-14:]}"

        if len(subcats) < 1:
            return f"Error: '{topcat}' subdictionary must have at least 1 key-value pair."

        for subcat, items in subcats.items():
            if not isinstance(items, list):
                return f"Error: '{subcat}' value is not a list. Content: {str(items)[:13]}...{str(items)[-14:]}"

            if len(items) < 1:
                return f"Error: '{subcat}' list must have at least 1 element."

            for item in items:
                if not isinstance(item, dict):
                    return f"Error: List element is not a dictionary. Content: {str(item)[:13]}...{str(item)[-14:]}"

                for key, value in item.items():
                    if key == 'title' and not isinstance(value, str):
                        return f"Error: 'title' value is not a string. Content: {str(value)[:13]}...{str(value)[-14:]}"
                    elif key in ['highlights', 'footer'] and not (
                            isinstance(value, list) and all(isinstance(v, str) for v in value)):
                        return f"Error: '{key}' value is not a list of strings. Content: {str(value)[:13]}...{str(value)[-14:]}"
                    elif key == 'body' and not (isinstance(value, str) or isinstance(value, go.Figure)):
                        return f"Error: 'body' value is not a string or a Plotly Figure object. Content: {str(value)[:13]}...{str(value)[-14:]}"
    return None