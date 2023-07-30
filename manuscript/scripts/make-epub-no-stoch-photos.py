import json
import datetime
import re

covers = {}


def copy_post(post):
    in_header = False

    lines = []

    image_line = ''
    skip_line = False

    with open('../' + post) as inputfile:
        for line in inputfile:
            if skip_line:
                merged_line = '![' + line.replace('*', '').replace('^', '').replace('\n', '') + image_line[2:]
                lines.append(merged_line)
                skip_line = False
            elif line.startswith('![]('):
                image_line = line
                skip_line = True
            else:
                lines.append(line)

    content = ''

    for line in lines:
        content += line

    while '\n\n\n' in content:
        content = content.replace('\n\n\n', '\n\n')

    with open('../epub/' + post, 'w') as html_file:
        html_file.write(content)


posts = ['2022-01-01-intro.markdown',
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
         '2022-06-14-leadership.markdown',
         '2022-06-15-career-paths.markdown',
         '2022-07-06-doing-architecture.markdown',
         '2022-07-07-culture-map.md',
         '2022-07-08-six-simple-rules.md',
         '2022-07-10-product.md',
         '2022-07-12-governance.markdown',
         '2022-07-15-economics.md',
         '2022-11-01-summary.markdown',
         '2022-11-04-cheat-sheet.markdown',
         '2022-11-24-bookshelf.markdown',
         '2022-11-24-tools.markdown',
         '2022-11-31-quotes.markdown',
         '2022-12-02-appendix.markdown',
         '2022-12-10-appendix-iso-25010.markdown',
         '2022-12-15-appendix-cloud.markdown',
         '2022-12-26-appendix-organization.markdown']

for post in posts:
    copy_post(post)
