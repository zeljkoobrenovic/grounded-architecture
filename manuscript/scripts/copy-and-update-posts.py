import json
import datetime
import re

covers = {}
def copy_post(post):
    content = ''

    in_header = False

    with open('../../_posts/' + post) as inputfile:
        for line in inputfile:
            if not in_header:
                if line.startswith('---') or line.startswith('<style') or line.startswith('<div class="quote"'):
                    if not '</div>' in line:
                        in_header = True
                    content += '\n\n'
                elif line.startswith('Image by'):
                    line = re.sub('<.*?>', '', line).replace('\n', '')
                    content += '\n^' + line.lower() + '^\n'
                elif line.startswith('<div'):
                    print('')
                elif line.startswith('</div'):
                    print('')
                    content += '\n'
                elif line.strip().startswith('> **IN THIS SECTION, YOU WILL'):
                    content += line[1:].strip() + '\n'
                elif line.strip() == '>':
                    print('')
                elif line.strip().startswith('> **KEY POINTS:') or line.strip().startswith('> ***KEY POINTS:'):
                    content += '\n{pagebreak}\n\n'
                    content += 'A' + line
                elif line.strip().startswith('</') or line.strip().startswith('<t'):
                    print('')
                elif line.strip().startswith('>'):
                    content += 'A' + line
                elif line.strip().startswith('<img') or line.strip().startswith('src='):
                    if 'src=' in line:
                        sub_line = line[line.index('src='):]
                        sub_line  = sub_line.replace('src="', '')
                        sub_line  = sub_line.replace('src=\'', '')
                        sub_line  = re.sub('".*', "", sub_line)
                        sub_line = sub_line.strip()
                        print('')
                        content += '\n![](' + sub_line + ')'
                elif not line.strip().startswith('<img') and not line.strip().startswith('src=') and not line.strip().startswith('style=') and not line.strip().startswith('<br'):
                    line = line.replace('](data)', '](#data)')
                    line = line.replace('](people)', '](#people)')
                    line = line.replace('](activities-platform)', '](#activities-platform)')
                    line = line.replace('](being-architect)', '](#being-architect)')
                    line = line.replace('](superglue)', '](#superglue)')
                    line = line.replace('](skills)', '](#skills)')
                    line = line.replace('](impact)', '](#impact)')
                    line = line.replace('](leadership)', '](#leadership)')
                    line = line.replace('](career)', '](#career)')
                    line = line.replace('](doing-architecture)', '](#doing-architecture)')
                    line = line.replace('](culture-map)', '](#culture-map)')
                    line = line.replace('](six-simple-rules)', '](#six-simple-rules)')
                    line = line.replace('](storm)', '](#storm)')
                    line = line.replace('](product-development)', '](#product-development)')
                    line = line.replace('](flexible-governance)', '](#flexible-governance)')
                    line = line.replace('](economics)', '](#economics)')
                    line = line.replace('](context)', '](#context)')
                    line = line.replace('](goals)', '](#goals)')
                    line = line.replace('](bookshelf)', '](#bookshelf)')
                    line = re.sub('<.*?>', '', line)
                    content += line
            else:
                if line.startswith('---') or line.startswith('</style>') or line.startswith('</div>'):
                    in_header = False
                elif line.startswith('title:'):
                    if (covers.get(post)):
                        content += '\n![](' +covers[post] + ')\n\n{pagebreak}\n\n'
                    content += '# ' + line.replace('title:', '').replace('"', '').strip()
                elif line.startswith('permalink:'):
                    content += ' {#' + line.replace('permalink:', '').replace('"', '').strip() + '}\n\n'

    while '\n\n\n' in content:
        content = content.replace('\n\n\n', '\n\n')

    while '\n\n^image by' in content:
        content = content.replace('\n\n^image by', '\n^image by')

    with open('../' + post, 'w') as html_file:
        html_file.write(content)


posts = ['2022-01-01-intro.markdown', '2022-01-02-context.markdown', '2022-01-03-requirements.markdown', '2022-03-01-grounded-architecture.markdown', '2022-03-03-data-platform.markdown', '2022-03-04-people.markdown',
         '2022-03-05-activities.markdown', '2022-03-09-value.markdown', '2022-06-01-being-architect.markdown', '2022-06-02-superglue.markdown', '2022-06-03-skills.markdown', '2022-06-10-impact.markdown', '2022-06-14-leadership.markdown',
         '2022-06-15-career-paths.markdown', '2022-07-06-doing-architecture.markdown', '2022-07-07-culture-map.md', '2022-07-08-six-simple-rules.md', '2022-07-10-product-trap.md',
         '2022-07-12-governance.markdown', '2022-07-15-economics.md', '2022-12-01-summary.markdown']


for post in posts:
    copy_post(post)
