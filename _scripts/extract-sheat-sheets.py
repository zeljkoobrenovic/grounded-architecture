import json
import datetime
import re


def extract_key_topics(post):
    content = ''
    found_topics = False
    in_header = False

    with open('../_posts/' + post) as inputfile:
        for line in inputfile:
            if not in_header:
                if not found_topics:
                    if line.strip().startswith('> **KEY POINTS:') or line.strip().startswith('> ***KEY POINTS:'):
                        in_header = True
                    elif line.startswith('title:'):
                        title = line.replace('title:', '').replace('"', '').strip()
                        if ': Introduction' in title:
                            content += '## ' + title + '\n\n'
                            in_header = False
                            found_topics = True
                        else:
                            content += '### ' + title + '\n'
            else:
                if line.strip().startswith('>'):
                    if len(line.strip()) > 1:
                        content += line
                else:
                    in_header = False
                    found_topics = True
                    content += '\n'

    while '\n\n\n' in content:
        content = content.replace('\n\n\n', '\n\n')

    return content

posts = ['2022-01-01-intro.markdown', '2022-01-02-context.markdown', '2022-01-03-requirements.markdown', '2022-03-01-grounded-architecture.markdown', '2022-03-03-data-platform.markdown', '2022-03-04-people.markdown',
         '2022-03-05-activities.markdown', '2022-03-09-value.markdown', '2022-06-01-being-architect.markdown', '2022-06-02-superglue.markdown', '2022-06-03-skills.markdown', '2022-06-10-impact.markdown', '2022-06-14-leadership.markdown',
         '2022-06-15-career-paths.markdown', '2022-07-06-doing-architecture.markdown', '2022-07-07-culture-map.md', '2022-07-08-six-simple-rules.md', '2022-07-10-product.md',
         '2022-07-12-governance.markdown', '2022-07-15-economics.md']


all_content = '## Introductions\n\n'

for post in posts:
    all_content += extract_key_topics(post)

with open('cheat-sheet.md', 'w') as html_file:
    html_file.write(all_content)
