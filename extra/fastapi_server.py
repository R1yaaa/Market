from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
from typing import List, Dict, Optional
import uvicorn
import uuid
import unolib
from unolib import Market, Account, User, Good

app = FastAPI()

accounts: Dict[str, str] = {} #Name und Passwort speichern

class UserModel(BaseModel):
    username: str
    password: str

class BuyGood(BaseModel):
    goodId: str
    quantity: int

class SellGood(BaseModel):
    goodId: str
    quantity: int    

@app.post("/register")
async def register(user: UserModel):
    try:
        print(f"DEBUG: User {user.username} trying to register")

        if user.username in accounts:
            print(f"DEBUG: User {user.username} exists already")
            raise HTTPException(status_code=406, detail="User already registered or occupied username")
        
        market.registerUser(user.username, user.password)
        accounts[user.username] = {"password": user.password}

        print(f"DEBUG: User {user.username} registered successfully")

        return {"message": f"{user.username} registered"}
    except Exception as e:
        print(f"ERROR registering: {e}")
        raise HTTPException(status_code=500, detail=f"Failed to register: {str(e)}")


@app.post("/login")
async def login(user: UserModel):
    try:
        print(f"DEBUG: User {user.username} trying to login")

        if user.username not in accounts:
            print(f"DEBUG: User {user.username} not found in accounts dict")
            raise HTTPException(status_code=404, detail="User not found")
        
        user_obj = accounts.get(user.username)
        if user_obj["password"] != user.password:
            print(f"DEBUG: {user.password} is not the same password")
            raise HTTPException(status_code=400, detail="incorrect password")
        
        market.loginUser(user.username, user.password)

        print(f"DEBUG: User {user.username} logged in successfully")

        return {"message": f"{user.username} logged in"}
    except Exception as e:
        print(f"ERROR logging in: {e}")
        raise HTTPException(status_code=500, detail=f"Failed to login: {str(e)}")
    

@app.get("/user/{username}/accountinfo")
async def accountinfo(username: str):
    try:
        user_obj = accounts.get(username)
        if not user_obj:
            print(f"DEBUG: {username} not found in accounts dict")
            raise HTTPException(status_code=404, detail="User not found")
        
        balance = account.getBalance()
        inventory = user.getInventory()

        return {
            "balance": balance,
            "inventory": inventory,
        }
    except Exception as e:
        print(f"ERROR showing account: {e}")
        raise HTTPException(status_code=500, detail=f"Failed to show Account: {str(e)}")


@app.get("/prices")
async def prices():
    try:
        prices = market.updatePrices()

        return {"prices": prices}
    except Exception as e:
        print(f"ERROR updating prices: {e}")
        raise HTTPException(status_code=500, detail=f"Failed to update prices: {str(e)}")

@app.get("/offers")
async def offers():
    try:
        goods = market.getOffers()

        return {"offers": goods}
    except Exception as e:
        print(f"ERROR showing offers: {e}")
        raise HTTPException(status_code=500, detail=f"Failed to show offers: {str(e)}")


@app.post("/buy")
async def buy(data: BuyGood, request: Request):
    try:
        print(f"DEBUG: Trying to buy {data.goodId}")

        username = request.headers.get("username")

        if market.getGood(data.goodId) == None:
            print("DEBUG: Good does not exist")
            raise HTTPException(status_code=404, detail="Good is not represented in the market")

        price = good.getCurrentPrice(data.goodId)    #parameter in hpp
        amount = price*data.quantity
        if account.hasEnoughBalance(amount) == False:
            print("DEBUG: Not enough money")
            raise HTTPException(status_code=400, detail="Not enough money")
        
        market.buyGood(data.goodId, data.quantity)

        balance = account.getBalance()
        inventory = user.getInventory()

        return {
            "inventory":inventory,
            "balance":balance,
        }
    except Exception as e:
        print(f"ERROR buying good: {e}")
        raise HTTPException(status_code=500, detail=f"Failed to buy good: {str(e)}")


@app.post("/sell")
async def sell(data: SellGood, request: Request):
    try:
        print(f"DEBUG: Trying to sell {data.goodId}")

        username = request.headers.get("username")

        if market.getGood(data.goodId) == None:
            print("DEBUG: Good does not exist")
            raise HTTPException(status_code=404, detail="Good is not represented in the market")

        anzahl = user.getGoodQuantity(data.goodId)
        if data.quantity > anzahl:
            print("DEBUG: Not enough in inventory")
            raise HTTPException(status_code=400, detail="Not enough goods in the inventory")

        market.sellGood(data.goodId, data.quantity) #methode in hpp hinzufügen

        balance = account.getBalance()
        inventory = user.getInventory()

        return {
                "inventory":inventory,
                "balance":balance,
            }
    except Exception as e:
        print(f"ERROR selling good: {e}")
        raise HTTPException(status_code=500, detail=f"Failed to sell good: {str(e)}")

#logout?
#nicht goodid, sondern name?
#klassen buygood und sellgood zu einer?

if __name__ == '__main__':
    uvicorn.run("fastapi_server:app", host="127.0.0.1", port=8000, reload=True)
