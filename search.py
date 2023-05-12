import pandas as pd
import numpy as np
import settings

from openai.embeddings_utils import get_embedding

datafile_path = "./data/structured-content-ada-002.csv"
df = pd.read_csv(datafile_path)
df["ada_embedding"] = df.ada_embedding.apply(eval).apply(np.array)

query="Wie legt man eine Aktionsliste an?"
query_embedding = get_embedding(query, engine=settings.EMBEDDING_MODEL, encoding=settings.EMBEDDING_ENCODING)
# compare the query embedding to the embeddings in the dataframe
df["similarity"] = df.ada_embedding.apply(lambda x: np.inner(x, query_embedding))
df = df.sort_values(by="similarity", ascending=False)
print(df.head(10))

