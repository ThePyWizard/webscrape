import requests
from bs4 import BeautifulSoup

# Fetch the HTML content (replace 'your_url' with the actual URL)
url = 'https://agri.py.gov.in/faq.html'
response = requests.get(url)
html_content = response.content

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Find all the question buttons and their corresponding answer panels
questions = soup.find_all('button', class_='accordion')
answers = soup.find_all('div', class_='panel')

# Open a text file to write the output with UTF-8 encoding
with open('questions_answers.txt', 'w', encoding='utf-8') as file:
    for question, answer in zip(questions, answers):
        # Extract the question text
        question_text = question.get_text(strip=True).replace('Question:', '').strip()
        
        # Extract the answer text
        answer_text = answer.get_text(strip=True).replace('Answers :', '').strip()
        
        # Write the question and answer to the file
        file.write(f"Question: {question_text}\n")
        file.write(f"Answer: {answer_text}\n")
        file.write("\n")

print("Questions and answers have been successfully saved to 'questions_answers.txt'")
