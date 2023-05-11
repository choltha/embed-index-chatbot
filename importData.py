# from https://github.com/openai/openai-cookbook/blob/main/examples/Obtain_dataset.ipynb

# imports
import pandas as pd
import tiktoken
import settings

from openai.embeddings_utils import get_embedding


# print(settings.OPENAI_API_KEY)



input_datapath = "./data/structured-content.csv"
df = pd.read_csv(input_datapath, index_col=0)
df = df[["Content"]]  # Adjusted column names here
df = df.dropna()
df["length"] = df.Content.apply(lambda x: len(x))
num_rows = len(df)
print(num_rows)
sorted_df = df.sort_values('length', ascending=False)

print(df.head(10))
print(sorted_df.head(10))

# Verify the column names after filtering
print(df.columns)

# show the length of each line

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