# Library Management System
## 🔍 **Project Overview**
This project is a **Menu-Driven Library Management System** developed using **Python** and **MySQL**.
It helps in managing books, issuing and returning books, and maintaining records of students who borrow books.
The system performs basic operations through Python using MySQL Connector.

---

## **Features Implemented**

-> Add new books to the library
-> Remove books using Book ID
-> Issue books to students
-> Return submitted books
-> Display all available books
-> Display all issued books
-> Input validation & error-handling
-> Real-time updates to MySQL database

---

##  **Project Structure**

```
Library-Management-System/
│
├── School Lib Management.py      # Main Python Program
├── README.md                      # Project Documentation
├── database.sql                   # SQL table creation script
├── Project_Report.txt             # Detailed report
├── /screenshots                   # Execution screenshots
```

---

##  **Database Details (MySQL)**

### **Database Name:** `library`

---

### **Table: `available_books`**

Stores all books with their current quantities.

| Column Name | Type            | Description            |
| ----------- | --------------- | ---------------------- |
| book_id     | INT PRIMARY KEY | Unique ID for the book |
| book_name   | VARCHAR(100)    | Title of the book      |
| subject     | VARCHAR(50)     | Category/subject       |
| quantity    | INT             | Number of copies       |

---

### **Table: `issued`**

Stores details of issued books.

| Column Name | Type        | Description         |
| ----------- | ----------- | ------------------- |
| book_id     | INT         | Book ID issued      |
| s_name      | VARCHAR(50) | Student name        |
| s_class     | VARCHAR(10) | Student class/grade |
| issue_date  | DATE        | Date of issue       |

---

## **SQL Table Creation Script (`database.sql`)**

```sql
CREATE DATABASE IF NOT EXISTS library;
USE library;

CREATE TABLE available_books (
    book_id INT PRIMARY KEY,
    book_name VARCHAR(100),
    subject VARCHAR(50),
    quantity INT
);

CREATE TABLE issued (
    book_id INT,
    s_name VARCHAR(50),
    s_class VARCHAR(10),
    issue_date DATE
);
```

---

## **How to Run the Project**

### Install Dependencies

```
pip install mysql-connector-python
```

### Start MySQL Server

### Update Credentials in Python File

```python
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="library"
)
```

### Run the Program

```
python "CS 12th Lib Management.py"
```

---

## **Menu Options in Program**

| Option | Function                  |
| ------ | ------------------------- |
| 1      | Add a new book            |
| 2      | Remove a book             |
| 3      | Issue a book to a student |
| 4      | Return a book             |
| 5      | Show available books      |
| 6      | Show issued book records  |
| 7      | Exit program              |

---

## **Testing**

* Added multiple books and verified entries in MySQL
* Tested issuing and returning books
* Ensured deletion works only if book exists
* Verified all menu options for incorrect input handling
* Checked SQL tables after each update

---

## **Screenshots**

All screenshots of program execution are stored inside the `/screenshots` folder.

---

## **Developed By**

**Rimi Vishwakarma**

---

## **Note**

This repository follows the required submission format:

* Contains README
* Contains screenshots folder
* Follows plagiarism-safe structure
* Code and documentation written manually
