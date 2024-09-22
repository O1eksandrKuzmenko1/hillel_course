import codecs
import re


def delete_html_tags(html_file, result_file='cleaned.txt'):
    with codecs.open(html_file, 'r', 'utf-8') as file:
        html = file.read()

    clean_text = re.sub(r'<[^>]+>', '', html)

    clean_text = '\n'.join(line.strip() for line in clean_text.splitlines() if line.strip())

    with codecs.open(result_file, 'w', 'utf-8') as file:
        file.write(clean_text)

    delete_html_tags('draft.html', 'cleaned.txt')