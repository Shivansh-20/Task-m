import sqlite3
connection = sqlite3.connect("trading.db")
cursor = connection.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS portfolio(
ticker TEXT,
quantity INT,
average_buyprice REAL  #like float
)
"""
)
connection.commit() #can use with for automatic but not good practise
connection.close()
