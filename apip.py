import sqlite3
from pydantic import BaseModel
from fastapi import FastAPI
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


    cursor.execute(
        "Select qauntity from portfolio where ticker = ?",
    (ticker,)
)
    row = cursor.fetchone


