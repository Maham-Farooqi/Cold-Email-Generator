import streamlit as st
from langchain_community.document_loaders import WebBaseLoader
from llama import chain
from chromaDb import FaissDb


def create_streamlit_app(llm, portfolio):
    st.title("📧 Cold Mail Generator")
    url_input = st.text_input("Enter a URL:", value="https://jobs.nike.com/job/R-46907")
    submit_button = st.button("Submit")

    if submit_button:
        try:
            loader = WebBaseLoader([url_input])
            data = loader.load().pop().page_content
            portfolio.store_data()
            jobs = llm.extract_jobs(data)
            print(jobs)
            for job in jobs:
                skills = job.get('skills', [])
                links = portfolio.query_db(skills,n_results=2)
                if not links:
                   print("No matching links found for skills:", skills)
                email = llm.write_mail(job, links)
                st.code(email, language='markdown')
        except Exception as e:
            st.error(f"An Error Occurred: {e}")


if __name__ == "__main__":
    chain = chain()
    portfolio = FaissDb(r'C:\Users\Lenovo\Desktop\python\coldEmailGenerator\resource\my_portfolio.csv')
    st.set_page_config(layout="wide", page_title="Cold Email Generator", page_icon="📧")
    create_streamlit_app(chain, portfolio)

