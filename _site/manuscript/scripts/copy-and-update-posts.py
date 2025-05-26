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
                                'grounded-architecture', 'analytics', 'people', 'operating-model',
                                'operating-model-principles', 'governance', 'transforming', 'gen-ai',
                                'being-architect', 'superglue', 'career-paths',
                                'skills', 'impact', 'leadership', 'leading-with-language', 'balancing',
                                'human-complexity', 'culture-map', 'six-simple-rules', 'human-decisions', 'effortless',
                                'strategy', 'ea-as-strategy', 'outsourcing',
                                'expanding-toolkit', 'economics', 'product', 'decision-intelligence', 'big-transformations',
                                'summary', 'appendix']

                    for section in sections:
                        fragment = '](' + section + ')'
                        if fragment in line:
                            line = line.replace(fragment, '](#' + section + ')')

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
    '2021-01-01-podcast.markdown',
    '2022-01-01-intro.markdown',
    '2022-01-02-context.markdown',
    '2022-01-03-requirements.markdown',
    '2022-03-01-grounded-architecture.markdown',
    '2022-03-03-data-platform.markdown',
    '2022-03-04-people.markdown',
    '2022-03-05-operating-model.markdown',
    '2022-03-08-principles.markdown',
    '2022-03-11-governance.markdown',
    '2022-03-18-value.markdown',
    '2022-03-20-gen-ai-operating-model.markdown',
    '2022-06-01-being-architect.markdown',
    '2022-06-02-superglue.markdown',
    '2022-06-03-career-paths.markdown',
    '2022-06-07-skills.markdown',
    '2022-06-10-impact.markdown',
    '2022-06-12-leadership.markdown',
    '2022-06-13-leading-with-language.markdown',
    '2022-06-16-balancing.markdown',
    '2022-07-01-human-complexity.md',
    '2022-07-03-culture-map.md',
    '2022-07-07-six-simple-rules.md',
    '2022-07-13-human-decisions.md',
    '2022-07-19-effortless.md',
    '2022-08-01-strategy.markdown',
    '2022-08-02-ea-as-strategy.md',
    '2022-08-05-outsourcing.md',
    '2022-09-20-expanding-toolkit.markdown',
    '2022-09-21-economics.md',
    '2022-09-23-product.md',
    '2022-09-26-decision-intelligence.md',
    '2022-09-29-big-transformations.md',
    '2022-11-01-summary.markdown',
    '2023-01-02-appendix.markdown'
]

counter = 0
for post in posts:
    counter += 1
    copy_post(post, counter)
