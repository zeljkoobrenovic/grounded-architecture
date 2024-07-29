import json
import datetime
import re

permalinks = ''


def extract_permalink(post, counter):
    print(str(counter) + '. ' + post)

    with open('../_posts/' + post) as inputfile:
        for line in inputfile:
            if line.strip().startswith('permalink:'):
                global permalinks
                permalinks += (line.replace('permalink:', '').strip() + '\n')
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
    '2022-09-20-organizations.markdown',
    '2022-09-23-product.md',
    '2022-09-24-governance.markdown',
    '2022-11-01-summary.markdown',
    '2022-12-02-appendix.markdown',
    '2022-12-03-appendix-quotes.markdown',
    '2022-12-04-appendix-bookshelf.markdown',
    '2022-12-05-appendix-career-resources.markdown',
    '2022-12-06-appendix-communication.md',
    '2022-12-08-appendix-tools.markdown',
    '2022-12-10-appendix-iso-25010.markdown',
    '2022-12-15-appendix-cloud.markdown',
    '2022-12-26-appendix-organization.markdown',
    '2022-12-29-appendix-data-website-techniques.markdown',
    '2022-12-30-appendix-cheat-sheet.markdown'
]

counter = 0

for post in posts:
    counter += 1
    extract_permalink(post, counter)

with open('permalinks.txt', 'w') as html_file:
    html_file.write(permalinks)
