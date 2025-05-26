import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from lib.db.connection import get_connection
from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.models.article import Article

def run_queries():
    print("Running example queries...")


    author = Author(name="Jane Doe")
    author.save()
    print(f"Created Author: {author.id} - {author.name}")


    magazine = Magazine(name="Tech Today", category="Technology")
    magazine.save()
    print(f"Created Magazine: {magazine.id} - {magazine.name} ({magazine.category})")

    
    article = author.add_article(magazine, "The Future of AI")
    print(f"Created Article: {article.id} - {article.title}")

    
    articles = author.articles()
    print(f"\nArticles by {author.name}:")
    for a in articles:
        print(f"- {a['title']} (ID: {a['id']})")

    
    magazines = author.magazines()
    print(f"\nMagazines contributed to by {author.name}:")
    for m in magazines:
        print(f"- {m['name']} (Category: {m['category']})")

    
    contributors = magazine.contributors()
    print(f"\nContributors to {magazine.name}:")
    for c in contributors:
        print(f"- {c['name']} (ID: {c['id']})")

if __name__ == "__main__":
    run_queries()
