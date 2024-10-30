import pymysql

class Restaurant:
    def __init__(self):
        self.connectToDatBase()
        self.createDataBase()
        self.createTable()
        self.insertIntoValues()

    def connectToDatBase(self):
        self.db = pymysql.connect(
            host = "localhost",
            user = "root",
            password = "0803"
        )
        self.cursor = self.db.cursor()

    def createDataBase(self):
        self.cursor.execute("CREATE DATABASE IF NOT EXISTS restaurant")
        self.cursor.execute("USE restaurant")

    def createTable(self):
        self.cursor.execute("DROP TABLE IF EXISTS restaurantTable")
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS restaurantTable(
                            id INT AUTO_INCREMENT PRIMARY KEY,
                            name text,
                            address text,
                            maxFoodPrice int,
                            minFoodPrice int,
                            employeesCount int,
                            experience int)""") 

    def insertIntoValues(self):
        self.cursor.execute("""INSERT INTO restaurantTable(name, address, maxFoodPrice, minFoodPrice, employeesCount, experience) VALUES
    ('Mirazur', 'Toshkent, Yakkasaroy tumani', 120000, 30000, 25, 12),
    ('Monar', 'Toshkent, Chilonzor tumani', 110000, 25000, 20, 10),
    ('Mamur', 'Samarqand, Registon kochasi', 90000, 20000, 15, 8),
    ('Afsona', 'Toshkent, Yunusobod tumani', 130000, 40000, 18, 15),
    ('Sahar', 'Buxoro, Gijduvon kochasi', 85000, 20000, 12, 6),
    ('Navbahor', 'Toshkent, Olmazor tumani', 100000, 30000, 22, 10),
    ('Mirzo', 'Namangan, Navbahor kochasi', 95000, 25000, 16, 9),
    ('Bonanza', 'Andijon, Shahar markazi', 140000, 50000, 30, 18),
    ('Marvorid', 'Toshkent, Bektemir tumani', 120000, 35000, 28, 14),
    ('Mavlono', 'Xiva, Ichan-qala', 110000, 30000, 21, 7)
""")
        self.db.commit()

    def showRestaurantsByName(self):
        self.cursor.execute("SELECT * FROM restaurantTable where name like 'm%r' ORDER BY maxFoodPrice")     
        result = self.cursor.fetchall()

        for data in result:
            print(data)    

    def showRestaurantsMinPrice(self):
        self.cursor.execute("SELECT name FROM restaurantTable ORDER BY minFoodPrice LIMIT 3")
        result = self.cursor.fetchall()

        for minPrice in result:
            print(minPrice)  

    def showRestaurantsByExperience(self):
        self.cursor.execute("SELECT * FROM restaurantTable ORDER BY experience DESC, maxFoodPrice LIMIT 4")
        result = self.cursor.fetchall()

        for experience in result:
            print(experience)

r1 = Restaurant()
r1.showRestaurantsByName()
r1.showRestaurantsMinPrice()
r1.showRestaurantsByExperience()