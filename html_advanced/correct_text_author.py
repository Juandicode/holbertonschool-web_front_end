from bs4 import BeautifulSoup

def check_testimonials(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    testimonials_section = soup.find('section', id='testimonials')
    
    if not testimonials_section:
        print("Testimonials section not found")
        return
    
    articles = testimonials_section.find_all('article')
    if len(articles) != 3:
        print("Expected 3 articles in Testimonials section")
        return
    
    expected_texts = [
        "I am completely blown away. Thanks to Techium, we've just launched our 5th website!",
        "Thank you so much for your help. Techium company is awesome!",
        "I love your system. Definitely worth the investment. I'd be lost without Techium company."
    ]
    expected_authors = ["Yuri Y.", "Dorrie S.", "Sven H."]
    
    for i, article in enumerate(articles):
        blockquote = article.find('blockquote')
        cite = article.find('cite')
        
        if not blockquote or not cite:
            print(f"Article {i+1} is missing blockquote or cite")
            continue
        
        text = blockquote.get_text(strip=True)
        author = cite.get_text(strip=True)
        
        print(f"Article {i+1} has correct text: {text == expected_texts[i]}")
        print(f"Article {i+1} author cited correctly: {author == expected_authors[i]}")

# Ejemplo de uso
with open('29-index.html', 'r') as file:
    html_content = file.read()
    check_testimonials(html_content)
