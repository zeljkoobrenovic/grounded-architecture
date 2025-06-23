import json
import datetime
import re

covers = {}


def copy_post(post):
    in_header = False

    lines = []

    image_line = ''
    skip_line = False

    special1 = '2022-11-24-bookshelf.markdown'
    special2 = '2022-11-24-tools.markdown'

    with open('../print/' + post) as inputfile:
        for line in inputfile:
            if post == special1 or post == special2:
                lines.append(line)
            elif skip_line:
                if len(line.strip()) > 0:
                    merged_line = '![' + line.replace('*', '').replace('^', '').replace('\n', '') + image_line[2:]
                    lines.append(merged_line)
                    skip_line = False
            elif line.startswith('![](') and not 'decision-policy.png' in line:
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


posts = [
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
    '2022-06-14-leading-with-language.markdown',
    '2022-06-16-balancing.markdown',
    '2022-06-20-preparing-for-ai.markdown',
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

for post in posts:
    copy_post(post)
