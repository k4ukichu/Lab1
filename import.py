from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
import csv


engine= create_engine('postgres://yzeeqrtrugucvb:9f14029371dc4742b2aabdeba4ce82468536eef4c5da208d18b60bb09af29686@ec2-184-73-243-101.compute-1.amazonaws.com:5432/d7c0g2ejfkih3q')
db = scoped_session(sessionmaker(bind=engine))

def main():

    db.execute("CREATE TABLE books (id SERIAL PRIMARY KEY,isbn VARCHAR NOT NULL, title VARCHAR NOT NULL, author VARCHAR NOT NULL, year INTEGER NOT NULL)")
    data_file=open("books.csv")
    reader=csv.reader(data_file)
    i=0
    for isbn,title,author,year in reader:
        if i==0: 
            i=1
            continue
        print(isbn,title,author,year)
        db.execute("INSERT INTO books (isbn,title,author,year) VALUES (:isbn, :title,:author,:year)",\
                   {"isbn":isbn,"title":title,"author":author,"year":year})

 
    db.execute("CREATE TABLE users (id SERIAL PRIMARY KEY, username VARCHAR NOT NULL, password VARCHAR NOT NULL, firstName VARCHAR NOT NULL, lastName VARCHAR NOT NULL)")

    db.commit()
if __name__=="__main__":
    main()
