import json
import datetime


def copy_post(post):
    content = ''

    in_header = False

    with open('../../_posts/' + post) as inputfile:
        for line in inputfile:
            print(line)
            if not in_header:
                if line.startswith('---') or line.startswith('<style'):
                    in_header = True
                    content += '{pagebreak}\n\n'
                else:
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
                    content += line
            else:
                if line.startswith('---') or line.startswith('</style>'):
                    in_header = False
                elif line.startswith('title:'):
                    content += '# ' + line.replace('title:', '').replace('"', '').strip()
                elif line.startswith('permalink:'):
                    content += ' {#' + line.replace('permalink:', '').replace('"', '').strip() + '}\n\n'

    with open('../' + post, 'w') as html_file:
        html_file.write(content)


posts = ['2022-01-01-intro.markdown', '2022-01-02-context.markdown', '2022-01-03-requirements.markdown', '2022-03-01-grounded-architecture.markdown', '2022-03-03-data-platform.markdown', '2022-03-04-people.markdown',
         '2022-03-05-activities.markdown', '2022-03-09-value.markdown', '2022-06-01-being-architect.markdown', '2022-06-02-superglue.markdown', '2022-06-03-skills.markdown', '2022-06-10-impact.markdown', '2022-06-14-leadership.markdown',
         '2022-06-15-career-paths.markdown', '2022-07-06-doing-architecture.markdown', '2022-07-07-culture-map.md', '2022-07-08-six-simple-rules.md', '2022-07-09-storm.markdown', '2022-07-10-product-trap.md',
         '2022-07-12-governance.markdown', '2022-07-15-economics.md', '2022-12-01-summary.markdown', '2022-12-04-cheat-sheet.markdown', '2022-12-24-bookshelf.markdown', '2022-12-24-tools.markdown', '2022-12-25-quotes.markdown']

for post in posts:
    copy_post(post)
