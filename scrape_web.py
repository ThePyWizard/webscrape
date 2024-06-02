import requests
from bs4 import BeautifulSoup

# Fetch the HTML content (replace 'your_url' with the actual URL)
url = 'https://ppqs.gov.in/faq?page=6'
response = requests.get(url, verify=False)  # Disable SSL verification
html_content = response.content

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Find all the question and answer pairs
questions_answers = soup.find_all('div', class_='views-row')

# Open a text file to write the output with UTF-8 encoding
with open('questions_answers.txt', 'a', encoding='utf-8') as file:
    for qa in questions_answers:
        # Extract the question text
        question_div = qa.find('div', class_='views-field-title')
        question = question_div.get_text(strip=True) if question_div else 'Question not found'
        
        # Extract the answer text
        answer_div = qa.find('div', class_='views-field-body')
        answer = answer_div.get_text(strip=True) if answer_div else 'Answer not found'
        
        # Write the question and answer to the file
        file.write(f"Question: {question}\n")
        file.write(f"Answer: {answer}\n")
        file.write("\n")

print("Questions and answers have been successfully saved to 'questions_answers.txt'")
