from lib.db.connection import get_connection

def seed():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.executescript("""
    DELETE FROM articles;
    DELETE FROM authors;
    DELETE FROM magazines;

    INSERT INTO authors (name) VALUES ('Alice Johnson'), ('Bob Smith');
    INSERT INTO magazines (name, category) VALUES ('Tech Today', 'Technology'), ('Health Weekly', 'Health');
    INSERT INTO articles (title, author_id, magazine_id) VALUES
        ('AI Innovations', 1, 1),
        ('Healthy Living Tips', 2, 2),
        ('Future of Robotics', 1, 1);
    """)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    seed()
