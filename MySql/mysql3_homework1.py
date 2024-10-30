import pymysql

class Core:
    def __init__(self):
        self.connectToDataBase()
        self.createDataBase()
        self.createTable()
        self.insertIntoValues()
        
    def connectToDataBase(self):
        self.db = pymysql.connect(
            host = "localhost",
            user = "root",
            password = "0803"
        )
        self.cursor = self.db.cursor()

    def createDataBase(self):
        self.cursor.execute("CREATE DATABASE IF NOT EXISTS company")
        self.cursor.execute("USE company")

    def createTable(self):
        self.cursor.execute("DROP TABLE company")
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS company(
                            id INT AUTO_INCREMENT PRIMARY KEY,
                            name text,
                            location text,
                            capital int,
                            employees_count int,
                            establishedAt int,
                            monthly_expenses int)""")
            
    def insertIntoValues(self):
        self.cursor.execute("""INSERT INTO company (name, location, capital, employees_count, establishedAt, monthly_expenses) VALUES
    ("Google", "AQSH", 245581, 200000, 1998, 300000),
    ("Visa", "AQSH", 34500, 20000, 2000, 150000),
    ("Apple", "AQSH", 2780000, 164000, 1976, 1500000),
    ("Samsung Electronics", "Janubiy Koreya", 500000, 287000, 1969, 1200000),
    ("Artel", "Tashkent", 500, 10000, 2011, 5000)""")
        self.db.commit() 
    
    def showCompanyNameByOrder(self):
        self.cursor.execute("SELECT * FROM company order by name")
        result = self.cursor.fetchall()
        print(result)

    def showCompanyCapitalByOrderDesc(self):
        self.cursor.execute("SELECT * FROM company ORDER BY capital DESC")
        result = self.cursor.fetchall()
        for capital in result:
            print(capital)  

    def showCompanyFewEmployees(self):
        self.cursor.execute("SELECT * FROM company ORDER BY employees_count LIMIT 1")
        result = self.cursor.fetchall()
        print(result) 

    def showCompanyLocationAtTashkent(self):
        self.cursor.execute("SELECT * FROM company WHERE location = 'Tashkent'")  
        result = self.cursor.fetchall()
        print(result)

    def showCompanyLocationCount(self):
        self.cursor.execute("SELECT location, COUNT(*) FROM company GROUP BY location")
        result = self.cursor.fetchall()
        for location, count in result:
            print(f"{location}:{count}")

    def showCompanyByExpenses(self):
        self.cursor.execute("SELECT * FROM company")
        result = self.cursor.fetchall()
        for company in result:
            expenses = (2024 - company[5]) * company[6]
            print(f"{company[1]}:{expenses}")


c1 = Core()        
c1.showCompanyNameByOrder()
c1.showCompanyCapitalByOrderDesc()
c1.showCompanyFewEmployees()
c1.showCompanyLocationAtTashkent()
c1.showCompanyLocationCount()
c1.showCompanyByExpenses()

