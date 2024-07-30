import json
import datetime
import re

covers = {}


def copy_post(post, counter):
    print(str(counter) + '. ' + post)

    content = ''

    in_header = False

    with open('../../_posts/' + post) as inputfile:
        for line in inputfile:
            if not in_header:
                if line.startswith('---') or line.startswith('<style') or line.startswith('<div class="quote"'):
                    if not '</div>' in line:
                        in_header = True
                    content += '\n\n'
                elif line.lower().startswith('image by'):
                    line = re.sub('<.*?>', '', line).replace('\n', '')
                    content += '\n^' + line.lower() + '^\n'
                elif line.startswith('<div'):
                    pass
                elif line.startswith('</div'):
                    content += '\n'
                elif line.strip().startswith('> **IN THIS SECTION, YOU WILL'):
                    content += line[1:].strip() + '\n'
                    content += '\n{pagebreak}\n\n'
                elif line.strip().startswith('#### The Mini-CEO'):
                    content += '\n{pagebreak}\n'
                    content += line + '\n'
                elif line.strip().startswith('#### The Former Project Manager'):
                    content += '\n{pagebreak}\n'
                    content += line + '\n'
                elif line.strip().startswith('#### The Waiter'):
                    content += '\n{pagebreak}\n'
                    content += line + '\n'
                elif line.strip().startswith('![](assets/images/economics/unsustainable-sw-dev.png)'):
                    content += '\n{pagebreak}\n'
                    content += line + '\n'
                elif line.strip() == '>':
                    pass
                elif line.strip().startswith('</') or line.strip().startswith('<t'):
                    pass
                elif line.strip().startswith('<blockq') or line.strip().startswith('<script'):
                    pass
                elif line.strip().startswith('>'):
                    content += 'A' + line
                elif line.strip().startswith('<img') or line.strip().startswith('src='):
                    if 'src=' in line:
                        sub_line = line[line.index('src='):]
                        sub_line = sub_line.replace('src="', '')
                        sub_line = sub_line.replace('src=\'', '')
                        sub_line = re.sub('".*', "", sub_line)
                        sub_line = sub_line.strip()
                        content += '\n![](' + sub_line + ')'
                elif not line.strip().startswith('<img') and not line.strip().startswith('src=') and not line.strip().startswith('style=') and not line.strip().startswith('<br'):
                    sections = ['intro', 'context', 'goals', 
                                'grounded-architecture', 'data', 'people', 'activities', 'transformation', 
                                'being-architect', 'superglue', 'skills', 'impact', 'career', 
                                'soft-skills', 'culture-map', 'leadership', 
                                'decision-making', 'decision-intelligence', 'human-decisions', 'economics', 
                                'complexity', 'effortless', 'six-simple-rules', 
                                'execution', 'product', 'governance'];

                    for section in sections:
                        line = line.replace('](' + section + ')', '](#' + section + ')')

                    line = re.sub('<.*?>', '', line)
                    content += line
            else:
                if line.startswith('---') or line.startswith('</style>') or line.startswith('</div>'):
                    in_header = False
                elif line.startswith('title:'):
                    if (covers.get(post)):
                        content += '\n![](' + covers[post] + ')\n\n{pagebreak}\n\n'
                    content += '# ' + line.replace('title:', '').replace('"', '').strip()
                elif line.startswith('permalink:'):
                    content += ' {#' + line.replace('permalink:', '').replace('"', '').strip() + '}\n\n'

    if post == '2022-11-04-cheat-sheet.markdown':
        content = content.replace('A> * ', '* ')
        content = content.replace('> * ', '* ')

    while '\n\n\n' in content:
        content = content.replace('\n\n\n', '\n\n')

    while '\n\n^image by' in content:
        content = content.replace('\n\n^image by', '\n^image by')

    with open('../' + post, 'w') as html_file:
        html_file.write(content)

    with open('../print/' + post, 'w') as html_file:
        html_file.write(content)


posts = [
    '2022-01-01-intro.markdown',
    '2022-01-02-context.markdown',
    '2022-01-03-requirements.markdown',
    '2022-03-01-grounded-architecture.markdown',
    '2022-03-03-data-platform.markdown',
    '2022-03-04-people.markdown',
    '2022-03-05-activities.markdown',
    '2022-03-09-value.markdown',
    '2022-06-01-being-architect.markdown',
    '2022-06-02-superglue.markdown',
    '2022-06-03-skills.markdown',
    '2022-06-10-impact.markdown',
    '2022-06-15-career-paths.markdown',
    '2022-07-01-soft-skills.markdown',
    '2022-07-03-culture-map.md',
    '2022-07-07-leadership.markdown',
    '2022-07-10-decision-making.markdown',
    '2022-07-12-decision-intelligence.md',
    '2022-07-13-human-decisions.md',
    '2022-07-15-economics.md',
    '2022-07-18-complexity.md',
    '2022-07-19-effortless.md',
    '2022-07-21-six-simple-rules.md',
    '2022-09-20-execution.markdown',
    '2022-09-23-product.md',
    '2022-09-24-governance.markdown',
    '2022-11-01-summary.markdown'
]

counter = 0
for post in posts:
    counter += 1
    copy_post(post, counter)
