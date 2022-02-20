# trustpilot


This project is about trustpilot reviews,we aim to scrap all elements in a specific category,and store it in an SQLite3 table.

A scrapy project was created with a regular spider using item loader and pipeline , the project is automated to store each category in a table exclusive for it with the same name

Note:the website is heavy loaded with Javascript so I had to use playwright to load the pages with virtual browser.

(Link of website)[https://www.trustpilot.com/]

**screenshot from financial_institution table
![Screenshot from 2022-02-20 18-21-03](https://user-images.githubusercontent.com/99041001/154852742-07a914e7-5bdc-4d65-9194-42e59e454cb6.png)

**screenshot from clothing_store table
![Screenshot from 2022-02-20 18-19-55](https://user-images.githubusercontent.com/99041001/154852748-42289493-25f6-4f0c-818c-4fa105bf6196.png)

**screenshot from bank table
![Screenshot from 2022-02-20 18-16-48](https://user-images.githubusercontent.com/99041001/154852749-5c0c002b-e552-44a8-a47c-35b8b90aacda.png)
