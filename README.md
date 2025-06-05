# Ask the Web 🔍

A simple web app that searches the internet and answers questions using AI.
*Loom Video link: https://www.loom.com/share/f6ec847ca25c4a66bb89fbd50b5a75df?sid=09cdf7ba-438d-49a1-883d-14bdca2dfe9d*

## What it does

You ask a question, it searches, scrapes websites, and gives you an answer with sources.

## Setup

```bash
git clone <repository-url>
cd ask_the_web
pip install -r requirements.txt
echo "GEMINI_API_KEY=your_key_here" > .env
streamlit run app.py
```

Or with Docker:
```bash
docker build -t ask-web .
docker run -p 8501:8501 ask-web
```

## How it works

```
User Question → Web Search → Scrape Websites → AI Answer
     ↓              ↓             ↓              ↓
  "What is AI?"  → Search Engine → Extract text → Gemini AI
```

## Architecture

```
app.py (Streamlit UI)
    ↓
web_search.py (DuckDuckGo API)
    ↓
scraper.py (Newspaper3k + BeautifulSoup)
    ↓
llm.py (Google Gemini)
```

## AI Prompts

**Main Answer LLM Prompt:**
```
"You are a smart assistant helping users answer questions using the provided documents.\n"
"Stick to the title and content of the documents.\n"
"If the question is not answerable with the documents, say 'I don't know about the topic'.\n"
"Use citations like [1], [2], etc. to refer to the documents.\n"
"Question: "
"Documents:\n"
"Answer:"
```

**Main Answer LLM Parameters:**
temperature = 0.5
max_output_tokens = 4096

*Rationale: Keep it simple so AI sticks to facts and cites sources properly with questions and supported documents in context. The LLM parameters restrict the hallucination risks*

## Testing

```bash
pytest test_scraper.py -v
```
![image](https://github.com/user-attachments/assets/3aa3a66f-315e-461e-a035-1c48503dae05)

Shows green (all tests pass).

## Tech Stack

- **Frontend:** Streamlit
- **Search:** DuckDuckGo Search API
- **Scraping:** Newspaper3k + BeautifulSoup
- **AI:** Google Gemini 2.0 Flash
- **Testing:** Pytest

## Known Limits

- **Search Results**: Only gets top 5 results 
- **Website Blocking**: Some sites block scraping (returns no content) which limits the sources to less than 5
- **Answer Quality**: Depends on search results being relevant
- **Load Time**: Takes 10-15 seconds per query
