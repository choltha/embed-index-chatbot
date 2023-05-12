# from https://github.com/openai/openai-cookbook/blob/main/examples/Obtain_dataset.ipynb

# imports
import pandas as pd
import tiktoken
import settings

from openai.embeddings_utils import get_embedding


# print(settings.OPENAI_API_KEY)



input_datapath = "./data/structured-content.csv"
df = pd.read_csv(input_datapath)
df = df[["Key","Content"]]  # Adjusted column names here
df = df.dropna()
df["length"] = df.Content.apply(lambda x: len(x))

print("Number of rows pre-split:")
num_rows = len(df)
print(num_rows)

#split long rows 

# Create an empty list to store the split chunks
split_chunks = []

encoding = tiktoken.get_encoding(settings.EMBEDDING_ENCODING)

#@todo not needed, so not testet (especially chunking length - needs better logic)
#@todo chunk at whitespace (or even period) to not chunk in mid-word
# Iterate over each row in the DataFrame
for index, row in df.iterrows():
    key = row['Key']
    content = row['Content']
    
    n_tokens = len(encoding.encode(content))

    if n_tokens > int(settings.EMBEDDING_MAX_TOKENS):
        # Split the content into chunks if too long
        chunks = [content[i:i+10000] for i in range(0, len(content), 10000)]
        
        # Append the chunks to the split_chunks list, modifying the key
        for i, chunk in enumerate(chunks):
            split_chunks.append({'Key': key, 'Content': chunk})
    else:
        # If the content length is less or equal append it as it is
        split_chunks.append({'Key': key, 'Content': content})

# Create a new DataFrame with the split chunks
chunked_df = pd.DataFrame(split_chunks)

chunked_df["length"] = chunked_df.Content.apply(lambda x: len(x))
chunked_df["tokens"] = chunked_df.Content.apply(lambda x: len(encoding.encode(x)) )

print("Number of rows post-split:")
num_rows = len(chunked_df)
print(num_rows)



#debug
#'''
sorted_df = chunked_df.sort_values('length', ascending=False)
sorted_df.to_csv("./data/split-content.csv")
print(sorted_df.head(10))
#'''

'''
print('test only')
df_test = chunked_df.head(1)
df_test = chunked_df.iloc[49:50]
print (df_test)
'''

sorted_df_final = sorted_df.copy()
#df_test['ada_embedding'] = df_test.Content.apply(lambda x: get_embedding(x, engine='text-embedding-ada-002'))
#df_test['ada_embedding'] = df_test['Content'].apply(lambda x: get_embedding(x, engine='text-embedding-ada-002'))
sorted_df_final['ada_embedding'] = sorted_df.Content.apply(lambda x: get_embedding(x, engine='text-embedding-ada-002'))
sorted_df_final.to_csv("./data/structured-content-ada-002.csv")

# Get embeddings and save them for future reuse
# Ensure you have your API key set in your environment per the README: https://github.com/openai/openai-python#usage
'''
# This may take a few minutes
df["embedding"] = df.Content.apply(lambda x: get_embedding(x, engine=embedding_model))
df.to_csv("data/fine_food_reviews_with_embeddings_1k.csv")
'''