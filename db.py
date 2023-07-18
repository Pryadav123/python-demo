import pymysql

conn = pymysql.connect(host='localhost', user='root',
                       password='Root@Pass1')

cursor = conn.cursor()
cursor.execute("""
SELECT world.country.Name, world.countrylanguage.Language  FROM world.countrylanguage
            left join world.country on world.country.Code = world.countrylanguage.CountryCode
            
            """
               )

row = cursor.fetchone()
while row:
    print(str(row[0]) + " " + str(row[1]))
    row = cursor.fetchone()