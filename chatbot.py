import settings
import search
import sys

# Assuming you want to read the first command-line argument
param = sys.argv[1]

print("Parameter:", param)

top_10=search.get_top_10_similar(param)
import tiktoken
