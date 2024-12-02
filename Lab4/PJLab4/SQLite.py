import sqlite3
from sqlite3 import Error

# Создаем соединение с базой данных
def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Successfully connected to SQLite Database")
    except Error as error:
        print(f"The error '{error}' occurred")
    return connection

# Подключаемся к базе данных
connection = create_connection(r"E:\LAB\Informatics\Lab4\table\library.sqlite")

# Создать таблицы
def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

# Создать таблицу книг
create_books_table = """
CREATE TABLE IF NOT EXISTS books (
    book_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    year_published INTEGER,
    quantity_available INTEGER
);
"""

#Создать таблицу участников
create_members_table = """
CREATE TABLE IF NOT EXISTS members (
    member_id INTEGER PRIMARY KEY AUTOINCREMENT,
    fullname TEXT NOT NULL,
    email TEXT NOT NULL,
    phone TEXT NOT NULL,
    join_date TEXT NOT NULL
);
"""

# Создать таблицу истории заимствований книг
create_borrowrecords_table = """
CREATE TABLE IF NOT EXISTS borrowrecords (
    borrow_id INTEGER PRIMARY KEY AUTOINCREMENT,
    book_id INTEGER NOT NULL,
    member_id INTEGER NOT NULL,
    borrow_date TEXT NOT NULL,
    return_date TEXT,
    status TEXT NOT NULL,
    FOREIGN KEY(member_id) REFERENCES members(member_id),
    FOREIGN KEY(book_id) REFERENCES books(book_id)
);
"""

# Создать таблицу отзывов
create_reviews_table = """
CREATE TABLE IF NOT EXISTS reviews (
    review_id INTEGER PRIMARY KEY AUTOINCREMENT,
    book_id INTEGER NOT NULL,
    member_id INTEGER NOT NULL,
    rating INTEGER CHECK (rating BETWEEN 1 AND 5),
    comment TEXT,
    review_date TEXT NOT NULL,
    FOREIGN KEY (book_id) REFERENCES books(book_id),
    FOREIGN KEY (member_id) REFERENCES members (member_id)
);
"""

execute_query(connection,create_books_table)
execute_query(connection,create_members_table)
execute_query(connection,create_borrowrecords_table)
execute_query(connection,create_reviews_table)

# Вставлять данные
create_books = """
INSERT INTO 
    books (title, author, year_published, quantity_available)
VALUES
    ('War and Peace', 'Leo Tolstoy', 1869, 10),
    ('Crime and Punishment', 'Fyodor Dostoevsky', 1866, 15),
    ('The Master and Margarita', 'Mikhail Bulgakov', 1967, 8),
    ('Anna Karenina', 'Leo Tolstoy', 1877, 12),
    ('Eugene Onegin', 'Alexander Pushkin', 1833, 20);
"""
execute_query(connection, create_books)

create_members = """
INSERT INTO 
    members (fullname, email, phone, join_date)
VALUES
    ('Phan', 'tandung@gmail.com', '+79211234567', '2023-01-15'),
    ('Anna', 'anna.ivanova@mail.ru', '+79217654321', '2023-03-22'),
    ('Dmitry', 'dmitry.smirnov@yandex.ru', '+79219876543', '2023-05-10'),
    ('Nguyen', 'nguyentan@gmail.com', '+79213456789', '2023-07-08'),
    ('Tran', 'tran.ngoc111@gmail.com', '+79214567890', '2023-09-30');
"""
execute_query(connection, create_members)

create_borrowrecords = """
INSERT INTO 
    borrowrecords (book_id, member_id, borrow_date, return_date, status)
VALUES
    (1, 2, '2024-01-15', '2023-01-30', 'returned'),
    (3, 1, '2024-03-20', '2023-04-05', 'returned'),
    (2, 4, '2024-05-01', '2023-05-20', 'overdue'),
    (5, 3, '2024-06-10', NULL, 'borrowed'),
    (4, 5, '2024-09-15', '2023-09-25', 'returned');
"""
execute_query(connection, create_borrowrecords)

create_reviews = """
INSERT INTO 
    reviews (book_id, member_id, rating, comment, review_date)
VALUES
    (1, 2, 5, 'An incredible masterpiece! Highly recommend.', '2024-01-20'),
    (3, 1, 4, 'Very intriguing, but a bit complex to follow.', '2024-03-25'),
    (2, 4, 3, 'Good book, but not my favorite.', '2024-05-15'),
    (5, 3, 5, 'A timeless classic! Truly enjoyed every page.', '2024-07-10'),
    (4, 5, 4, 'Engaging story with deep character development.', '2024-09-05');
"""
execute_query(connection, create_reviews)

# Bыбрать все записи из таблиц
def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")

select_books = "SELECT * FROM books"
books = execute_read_query(connection, select_books)
for book in books:
    print(book)
print("\n")

select_members = "SELECT * FROM members"
members = execute_read_query(connection, select_members)
for member in members:
    print(member)
print("\n")

select_borrowrecords = "SELECT * FROM borrowrecords"
borrowrecords = execute_read_query(connection, select_borrowrecords)
for borrowrecord in borrowrecords:
    print(borrowrecord)
print("\n")

select_reviews = "SELECT * FROM reviews"
reviews = execute_read_query(connection, select_reviews)
for review in reviews:
    print(review)
print("\n")

#составить запрос по извлечению данных с использованием JOIN
select_books_reviews = """
SELECT
    books.title,
    members.fullname,
    reviews.comment
FROM
    books
INNER JOIN reviews ON books.book_id = reviews.book_id
INNER JOIN members ON members.member_id = reviews.member_id
"""
books_reviews = execute_read_query(connection, select_books_reviews)
for books_review in books_reviews:
    print(books_review)
print("\n")

# составить запрос по извлечению данных с использованием WHERE и GROUP BY
select_avg_rating = """
SELECT 
    books.title,
    AVG(reviews.rating) AS average_rating
FROM books,
    reviews
WHERE 
    books.book_id = reviews.book_id
GROUP BY 
    books.title;
"""

avg_ratings = execute_read_query(connection, select_avg_rating)
for avg_rating in avg_ratings:
    print(avg_rating)
print("\n")

#Составить два запроса, в которых будет вложенный SELECT-запрос (вложение с помощью WHERE.)
select_borrowrecords_for_books_after_1900 = """
SELECT * 
FROM
    borrowrecords
WHERE
    book_id IN (
        SELECT book_id
        FROM books
        WHERE books.year_published > 1900
    );
"""
borrowrecords_after_1900 = execute_read_query(connection, select_borrowrecords_for_books_after_1900)
print("Borrowrecords for Books Published After 1900:")
for borrowrecord in borrowrecords_after_1900:
    print(borrowrecord)
print("\n")

select_reviews_for_author = """
SELECT *
FROM reviews
WHERE book_id IN (SELECT book_id FROM books WHERE author = 'Leo Tolstoy');
"""
reviews_for_author = execute_read_query(connection, select_reviews_for_author)
print("Reviews for Books by Leo Tolstoy:")
for review in reviews_for_author:
    print(review)
print("\n")

# UNION Query 1
select_union_query_1 = """
SELECT 
    book_id,
    member_id
FROM 
    borrowrecords
UNION
SELECT 
    book_id,
    member_id
FROM 
    reviews
"""
union1_result = execute_read_query(connection, select_union_query_1)
for record1 in union1_result:
    print(record1)
print("\n")

# UNION Query 2
select_union_query_2 = """
SELECT title
FROM books
JOIN reviews ON books.book_id = reviews.book_id
WHERE reviews.rating > 4
UNION
SELECT title
FROM books
JOIN reviews ON books.book_id = reviews.book_id
WHERE reviews.rating <= 3;
"""
union2_result = execute_read_query(connection, select_union_query_2)
for record2 in union2_result:
    print(record2)
print("\n")

# DISTINCT Query
select_distinct_query = """
SELECT DISTINCT author
FROM books;
"""
distinct_result = execute_read_query(connection, select_distinct_query)
print("Distinct Authors:")
for author in distinct_result:
    print(author)
print("\n")

# Обновить две записи в двух разных таблицах Вашей базы данных
update_book_publication_year = """
UPDATE books
SET year_published = 2000
WHERE title = 'War and Peace';
"""
execute_query(connection, update_book_publication_year)

update_email_member = """
UPDATE members
SET email = "tandung10404@gmail.com"
WHERE fullname = 'Phan';
"""
execute_query(connection, update_email_member)

# Удалить по одной записи из каждой таблицы.
delete_book_query = """
DELETE FROM books
WHERE book_id = 1; 
"""
execute_query(connection, delete_book_query)

delete_member_query = """
DELETE FROM members
WHERE member_id = 1; 
"""
execute_query(connection, delete_member_query)

delete_borrowrecord_query = """
DELETE FROM borrowrecords
WHERE borrow_id = 1; 
"""
execute_query(connection, delete_borrowrecord_query)

delete_review_query = """
DELETE FROM reviews
WHERE review_id = 1; 
"""
execute_query(connection, delete_review_query)

# Удалить все записи в одной из таблиц
delete_all_books_query = """
DELETE FROM books;
"""
execute_query(connection, delete_all_books_query)
