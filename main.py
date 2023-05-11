# using https://github.com/openai/openai-cookbook/blob/main/examples/Question_answering_using_embeddings.ipynb
# imports
import ast  # for converting embeddings saved as strings back to arrays
import openai  # for calling the OpenAI API
import pandas as pd  # for storing text and embeddings data
import tiktoken  # for counting tokens
from scipy import spatial  # for calculating vector similarities for search

import settings