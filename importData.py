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

# Iterate over each row in the DataFrame
for index, row in df.iterrows():
    key = row['Key']
    content = row['Content']
    
    # Check if the content length exceeds 2000 characters
    if len(content) > 2000:
        # Split the content into chunks of maximum 2000 characters
        chunks = [content[i:i+2000] for i in range(0, len(content), 2000)]
        
        # Append the chunks to the split_chunks list, modifying the key
        for i, chunk in enumerate(chunks):
            split_chunks.append({'Key': key, 'Content': chunk})
    else:
        # If the content length is less than or equal to 2000 characters, append it as it is
        split_chunks.append({'Key': key, 'Content': content})

# Create a new DataFrame with the split chunks
chunked_df = pd.DataFrame(split_chunks)

chunked_df["length"] = chunked_df.Content.apply(lambda x: len(x))

# debug
# sorted_df = chunked_df.sort_values('length', ascending=False)
# sorted_df.to_csv("./data/split-content.csv")
# print(sorted_df.head(50))




'''
# subsample to 1k most recent reviews and remove samples that are too long
top_n = 1000
df = df.sort_values("Time").tail(top_n * 2)  # first cut to first 2k entries, assuming less than half will be filtered out
df.drop("Time", axis=1, inplace=True)

encoding = tiktoken.get_encoding(embedding_encoding)

# omit reviews that are too long to embed
df["n_tokens"] = df.combined.apply(lambda x: len(encoding.encode(x)))
df = df[df.n_tokens <= max_tokens].tail(top_n)
len(df)

# Get embeddings and save them for future reuse
# Ensure you have your API key set in your environment per the README: https://github.com/openai/openai-python#usage

# This may take a few minutes
df["embedding"] = df.combined.apply(lambda x: get_embedding(x, engine=embedding_model))
df.to_csv("data/fine_food_reviews_with_embeddings_1k.csv")
'''