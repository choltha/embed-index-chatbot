import pandas as pd
import numpy as np
import settings

from openai.embeddings_utils import get_embedding


def get_top_10_similar(query):
    datafile_path = "./data/structured-content-ada-002.csv"
    df = pd.read_csv(datafile_path)
    df["ada_embedding"] = df.ada_embedding.apply(eval).apply(np.array)

    # get the embedding for the query
    query_embedding = get_embedding(query, engine=settings.EMBEDDING_MODEL, encoding=settings.EMBEDDING_ENCODING)
    # compare the query embedding to the embeddings in the dataframe
    df["similarity"] = df.ada_embedding.apply(lambda x: np.inner(x, query_embedding))
    df = df.sort_values(by="similarity", ascending=False)
    return df.head(10)

if __name__ == "__main__":
    query = "How do i create an action list?"
    print(get_top_10_similar(query))

