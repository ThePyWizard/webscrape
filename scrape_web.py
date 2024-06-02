import requests
from bs4 import BeautifulSoup

# Fetch the HTML content (replace 'your_url' with the actual URL)
url = 'https://agriinfra.dac.gov.in/Home/FAQs'
response = requests.get(url)
html_content = response.content

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Find all the question and answer pairs
questions_answers = soup.find_all('div', class_='card')

# Open a text file to write the output with UTF-8 encoding
with open('questions_answers.txt', 'w', encoding='utf-8') as file:
    for card in questions_answers:
        # Extract the question
        question_header = card.find('div', class_='card-header')
        if question_header:
            question_button = question_header.find('button')
            question = question_button.get_text(strip=True) if question_button else 'Question not found'
        else:
            question = 'Question not found'
        
        # Extract the answer
        answer_div = card.find('div', class_='card-body')
        answer = answer_div.get_text(strip=True) if answer_div else 'Answer not found'
        
        # Write the question and answer to the file
        file.write(f"Question: {question}\n")
        file.write(f"Answer: {answer}\n")
        file.write("\n")

print("Questions and answers have been successfully saved to 'questions_answers.txt'")
