from fastapi import FastAPI

app = FastAPI (
    title="Xử lý danh sách theo trạng thái",
    description="API trả về danh sách theo trạng thái"
)

books = [
    {
        "id": 1,
        "title": "Python Basic",
        "author": "Lê Minh Thu",
        "category": "programming",
        "year": 2022,
        "is_available": True
    },
    {
        "id": 2,
        "title": "Web API Design",
        "author": "Phạm Lan Hồng",
        "category": "web",
        "year": 2021,
        "is_available": False
    },
    {
        "id": 3,
        "title": "Database System",
        "author": "Lê Minh Huyền",
        "category": "database",
        "year": 2020,
        "is_available": True
    },
    {
        "id": 4,
        "title": "Clean Code",
        "author": "Lê Ánh Linh",
        "category": "programming",
        "year": 2008,
        "is_available": False

    },
    {
        "id": 5,
        "title": "Computer Network",
        "author": "Vũ Hồng Vân",
        "category": "network",
        "year": 2019,
        "is_available": True
    }
]

@app.get('/books/statistics')
def get_books_statistics():
    count_avaliable = 0
    count_borrowed = 0

    for book in books:
        if book["is_available"] is True:
            count_avaliable += 1

        else:
            count_borrowed += 1

    return {
        "total_books": len(books),
        "available_books": count_avaliable,
        "borrowed_books": count_borrowed
    }

@app.get("/books/categories")
def get_books_categories():
    lst = []

    for book in books:
        if book["category"] not in lst:
            lst.append(book['category'])

    return lst

@app.get("/books/latest")
def get_books_latest():
    if not books:
        return {
            "message": "No books available"
        }
    
    max = books[0]

    for book in books:
        if max['year'] < book['year']:
            max = book

    return {
        'message': max
    }
