import requests
from bs4 import BeautifulSoup

# Replace with the actual URL of the webpage you want to scrape
url = 'https://www.investindia.gov.in/faqs/sectoral'

# Send a GET request to fetch the raw HTML content
response = requests.get(url)

# Parse the content with BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find the container that holds the Q&A items
view_content = soup.find('div', class_='view-content')

# Check if the container exists
if view_content:
    # Find all the Q&A items
    items = view_content.find_all('li', class_='accordion-row')
    
    if items:
        print(f"Found {len(items)} items")
        
        # Loop through each item to extract the question and answer
        qa_list = []
        for item in items:
            question = item.find('div', class_='accordion-section-title').get_text(strip=True)
            answer = item.find('div', class_='accordion-section-content').get_text(strip=True)
            qa_list.append({'question': question, 'answer': answer})
        
        # Save the Q&A pairs to a file
        with open('qa_data.txt', 'w', encoding='utf-8') as f:
            for qa in qa_list:
                f.write(f"Q: {qa['question']}\n")
                f.write(f"A: {qa['answer']}\n")
                f.write("\n")
        
        print("Q&A pairs saved to qa_data.txt")
    else:
        print("No Q&A items found")
else:
    print("Q&A container not found")
