# Cold Email Generator

The Cold Email Generator is a Python-based **Streamlit web application** that generates personalized cold emails based on job postings from a given URL. This tool is designed to help job seekers craft tailored emails efficiently, leveraging AI and automation.

---

## Features
- Extract job details from a URL.
- Generate personalized cold emails for job applications.
- Simple, user-friendly interface built with Streamlit.
- JSON parsing for structured data extraction.
- Error handling for invalid URLs or unexpected data formats.

---

## Requirements

Before running the application, ensure you have the following:

### Prerequisites
- Python 3.8+
- Streamlit
- Additional libraries:
  - `requests`
  - `json`
  - `langchain` (for AI-powered email generation)

### Steps to Generate Cold Emails
1. Enter the URL of a job posting.
2. Click the "Generate Email" button.
3. View or copy the generated email.

---

## Code Overview

### Core Functionality
- **Extract Metadata**: The script uses the `requests` library to fetch the content of the job posting.
- **Parse Job Details**: Extracts job title, company name, and requirements from the webpage.
- **Generate Email**: Uses AI to generate a professional and tailored email based on the extracted information.
