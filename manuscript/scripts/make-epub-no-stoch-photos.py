import json
import datetime
import re

covers = {}
def copy_post(post):
    in_header = False

    lines = []

    with open('../print/' + post) as inputfile:
        for line in inputfile:
            if line.startswith('^image by'):
                lines.pop()
            elif line.startswith('![](assets/images/superglue/superglue.png)'):
                print('![](assets/images/superglue/superglue.png)')
            else:
                lines.append(line)

    content = ''

    for line in lines:
        content += line

    while '\n\n\n' in content:
        content = content.replace('\n\n\n', '\n\n')

    with open('../epub/' + post, 'w') as html_file:
        html_file.write(content)


posts = ['2022-01-01-intro.markdown', '2022-01-02-context.markdown', '2022-01-03-requirements.markdown', '2022-03-01-grounded-architecture.markdown', '2022-03-03-data-platform.markdown', '2022-03-04-people.markdown', '2022-03-05-activities.markdown', '2022-03-09-value.markdown', '2022-06-01-being-architect.markdown', '2022-06-02-superglue.markdown', '2022-06-03-skills.markdown', '2022-06-10-impact.markdown', '2022-06-14-leadership.markdown', '2022-06-15-career-paths.markdown', '2022-07-06-doing-architecture.markdown', '2022-07-07-culture-map.md', '2022-07-08-six-simple-rules.md', '2022-07-10-product-trap.md', '2022-07-12-governance.markdown', '2022-07-15-economics.md', '2022-12-01-summary.markdown', '2022-12-04-cheat-sheet.markdown', '2022-12-24-bookshelf.markdown', '2022-12-24-tools.markdown', '2022-12-25-quotes.markdown']


for post in posts:
    copy_post(post)