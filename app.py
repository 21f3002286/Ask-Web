import streamlit as st
import web_search
import scraper
import llm

# Enhanced CSS styling with dark theme matching the space background
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(rgba(20, 24, 35, 0.8), rgba(46, 134, 171, 0.3)), 
                    url('https://images.unsplash.com/photo-1451187580459-43490279c0fa?ixlib=rb-4.0.3&auto=format&fit=crop&w=2072&q=80');
        background-size: cover;
        background-attachment: fixed;
        background-position: center;
        color: #E8E8E8;
    }
    
    .main-title {
        text-align: center;
        color: #4FC3F7;
        margin-bottom: 30px;
        font-weight: bold;
        text-shadow: 2px 2px 8px rgba(79, 195, 247, 0.3);
        font-size: 3rem;
    }
    
    .answer-box {
        background-color: rgba(30, 41, 59, 0.95);
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #4FC3F7;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
        backdrop-filter: blur(10px);
        color: #F0F0F0;
    }
    
    .stTextInput > div > div > input {
        background-color: rgba(30, 41, 59, 0.9) !important;
        border-radius: 8px !important;
        border: 2px solid #4FC3F7 !important;
        color: #E8E8E8 !important;
    }
    
    .stTextInput label {
        color: #E8E8E8 !important;
    }
    
    .stButton > button {
        background-color: #4FC3F7 !important;
        color: #1E293B !important;
        border-radius: 8px;
        border: none;
        font-weight: bold;
        box-shadow: 0 2px 4px rgba(79, 195, 247, 0.3);
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        background-color: #29B6F6 !important;
        box-shadow: 0 4px 12px rgba(79, 195, 247, 0.5);
        transform: translateY(-2px);
    }
    
    .stSpinner > div {
        border-top-color: #4FC3F7 !important;
    }
    
    .stExpander {
        background-color: rgba(30, 41, 59, 0.9) !important;
        border-radius: 8px;
        border: 1px solid rgba(79, 195, 247, 0.5);
    }
    
    .stExpander label {
        color: #E8E8E8 !important;
    }
    
    /* Style for error messages */
    .stAlert {
        background-color: rgba(30, 41, 59, 0.9) !important;
        color: #F0F0F0 !important;
    }
    
    /* Style for warning messages */
    .stWarning {
        background-color: rgba(30, 41, 59, 0.9) !important;
        color: #FFC107 !important;
    }
    
    /* Style for success messages */
    .stSuccess {
        background-color: rgba(30, 41, 59, 0.9) !important;
        color: #4CAF50 !important;
    }
    
    /* JSON viewer in debug section */
    .stJson {
        background-color: rgba(15, 23, 42, 0.95) !important;
        color: #E8E8E8 !important;
    }
    
    /* General text color */
    p, div, span {
        color: #E8E8E8 !important;
    }
    
    /* Headings */
    h1, h2, h3, h4, h5, h6 {
        color: #4FC3F7 !important;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<h1 class="main-title">Ask the Web 🔍</h1>', unsafe_allow_html=True)

question = st.text_input("Enter your question:")
if st.button("Ask"):
    if question:
        # Search
        with st.spinner("Searching the web..."):
            results = web_search.web_search(question, max_results=3)
        
        if results:
            # Scrape
            with st.spinner("Getting content from websites..."):
                documents = []
                for result in results:
                    try:
                        scraped = scraper.text_scraper(result['href'])
                        if scraped:
                            documents.append(scraped)
                    except:
                        pass
            
            if documents:
                # Generate answer
                with st.spinner("Generating answer..."):
                    answer = llm.generate_answer(question, documents)
                
                st.markdown('<div class="answer-box">', unsafe_allow_html=True)
                st.write("### Answer:")
                st.write(answer)
                st.markdown('</div>', unsafe_allow_html=True)
                
                # Debug info
                with st.expander("Debug Info"):
                    st.json(results)
            else:
                st.error("Could not get content from websites")
        else:
            st.error("No search results found")
    else:
        st.warning("Please enter a question")