import json
import datetime
import re

permalinks = []


def extract_permalink(post, counter):
    print(str(counter) + '. ' + post)

    with open('../_posts/' + post) as inputfile:
        for line in inputfile:
            if line.strip().startswith('permalink:'):
                global permalinks
                permalinks.append(line.replace('permalink:', '').strip())
                break


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
    '2022-09-24-governance.markdown'
]

counter = 0

for post in posts:
    counter += 1
    extract_permalink(post, counter)

with open('permalinks.txt', 'w') as html_file:
    html_file.write( json.dumps(permalinks))
