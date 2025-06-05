from duckduckgo_search import DDGS

def web_search(query: str, max_results=5):
    ddgs = DDGS()
    # returns a list of dictionaries with Top 5 search results
    return list(ddgs.text(query, max_results=max_results))

# if __name__ == "__main__":
#     print(web_search("Python programming"))