import json
import datetime
import re

prompts_root = '/Users/zeljkoobrenovic/PycharmProjects/grounded-architecture-dashboard-examples/ai-prompts/'
prompts = json.load(open('%sdata/index.json' % prompts_root))

prompts_text = ''

for group in prompts:
    for prompt in group['prompts']:
        prompt_content = open(prompts_root + 'docs/' + prompt['file']).read()

        prompts_text += '<br>\n## ' + prompt['name'] + '\n\n'
        prompts_text += '' + prompt['description'] + '\n\n'

        prompts_text += '\n\n**Prompt**:\n\n'
        prompts_text += '> ' + re.sub('\n', '\n> ', prompt_content) + '`\n\n'

        prompts_text += '\n\n<br>**Example files to provide as input**:\n\n'
        for attachment in prompt['attachments']:
            prompts_text += '- [' + attachment['label'] + '](' + attachment['href'] + ')\n'

        prompts_text += '\n\n\n'

with open('../../_posts/2022-12-28-appendix-gen-ai-prompts.markdown', 'w') as html_file:
    template = open('templates/2022-12-28-appendix-gen-ai-prompts.markdown').read()
    content = template.replace('${generated-text}', prompts_text)
    html_file.write(content)
