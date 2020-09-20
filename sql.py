# model for our blog project 
import sqlite3

#creating a new database if the database doesn't already exist
with sqlite3.connect("blog.db") as connection:
    #get a cursor object used to execute the sql commands
    c = connection.cursor()


    #create table
    c.execute("""CREATE TABLE IF NOT EXISTS posts(title TEXT, post TEXT)""")


    #inserting the dummy data into the table 
    c.execute('INSERT INTO posts VALUES("Good", "I\'m good.")')
    c.execute('INSERT INTO posts VALUES("Well", "I\'m well.")')
    c.execute('INSERT INTO posts VALUES("Excellent", "I\'m excellent.")')
    c.execute('INSERT INTO posts VALUES("Okay", "I\'m okay.")')
