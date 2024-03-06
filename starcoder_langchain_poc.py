from langchain_community.llms import HuggingFaceEndpoint

sc2_3b = HuggingFaceEndpoint(
    repo_id = "bigcode/starcoder2-3b",
    temperature= 0.1
)

sc2_15b = HuggingFaceEndpoint(
    repo_id = "bigcode/starcoder2-15b",
    temperature= 0.1
)