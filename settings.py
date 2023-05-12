import os
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]

EMBEDDING_MODEL = "text-embedding-ada-002"
EMBEDDING_ENCODING = "cl100k_base" # this the encoding for text-embedding-ada-002
EMBEDDING_MAX_TOKENS = "8191" # the maximum for text-embedding-ada-002 is 8191

GPT_MODEL = "gpt-3.5-turbo"
GPT_MAX_TOKENS = "4096" # the maximum for gpt-3.5-turbo is 4096 - see https://platform.openai.com/docs/guides/chat/introduction
