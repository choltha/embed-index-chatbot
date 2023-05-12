import settings
import search
import sys
import pandas as pd
import yaml
import openai

# Assuming you want to read the first command-line argument
template_config = sys.argv[1]
user_query = sys.argv[2]

print("template_config:", template_config)
print("user_query:", user_query)
#print(openai.api_key)

total_tokens = int(settings.GPT_MAX_TOKENS_FULL_PROMPT)
answer_token_placeholder = 500
fewshot_guidance_token = 1000
token_for_content = total_tokens - answer_token_placeholder - fewshot_guidance_token
#print (token_for_content) # should be 2596

df_top_10=search.get_top_10_similar(user_query)
print(df_top_10)

concatenated_text = ""
total_tokens_added = 0

# Iterate over each row in the DataFrame
# adding the content to the concatenated_text
# until the total tokens added would exceed the max token_for_content

for index, row in df_top_10.iterrows():
    print(row)
    text = row['Content']
    tokens = row['tokens']

    if total_tokens_added + tokens <= token_for_content:
        concatenated_text += text + " "
        total_tokens_added += tokens
    else:
        break
print ("Total Tokens Added:", total_tokens_added)
print("Concatenated Text:", concatenated_text)

# import promt template
with open('./prompt-templates/manual.txt', 'r') as file:
    template = file.read()

# import template config
with open(template_config, 'r') as file:
    template_data = yaml.safe_load(file)

# data which is not in the template config
additional_data = {
    'reference_data': concatenated_text
}
# Combine the data from the YAML file and the additional data into a single dictionary:
data = {**template_data, **additional_data}

# fill in the placeholders
completed_template = template.format(**data)
print(completed_template)
print("##############")

# run gpt query

messages=[ 
     {"role": "system", "content": completed_template},
     {"role": "user", "content": user_query}
     ]

print(openai.ChatCompletion.create(
    model=settings.GPT_MODEL,
    messages=messages,
    max_tokens=200, 
    temperature = 0.7,
    stream = False
    ))

# show results

