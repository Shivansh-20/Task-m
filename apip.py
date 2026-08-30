import sqlite3
from pydantic import BaseModel
from fastapi import FastAPI
connection = sqlite3.connect("trading.db")
cursor = connection.cursor()
#://github.com/Shivansh-20/Task-m/blame/main/manual(apip)#L1-L20
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
prices = {
    "TCS":3900,
    "INFO":3000,
    "HCL":2800
}
class Trade(BaseModel):
    ticker: str
    quantity: int


app = FastAPI()

@app.post("/trade")
def trade_stock(trade:Trade):
    ticker = trade.ticker
    quantity = trade.quantity
    price = prices[ticker] #store the value in price from dict price of company in ticker
    total = quantity * price 

    cursor.execute(
        "Select qauntity from portfolio where ticker = ?",
    (ticker,)
)
    row = cursor.fetchone
    if row is None:
        cursor.execute(
        """
            insert into portfolio (ticker,quantity,average_price)
            values(?,?,?)
        """,
        (ticker,quantity,price)
        )
    else:
        new_quantity = row[0] + quantity
        cursor.execute(
        """ 
             update portfolio
             set quantity = ?
             where ticker = ?
        """,
        (new_quantity,ticker)
        )
    connection.commit()
    connection.close()
    return {                            #why not ()
        "ticker": ticker,
        "quantity_bought": quantity,
        "price":price,
        "total":total
    } 

    


