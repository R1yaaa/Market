from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
from typing import List, Dict, Optional
import uvicorn
import uuid
import unolib
from unolib import Market, Account, User, Good

import sys
sys.path.append("../build")  # Pfad zur kompilierten unolib

app = FastAPI()

market = Market()


class UserModel(BaseModel):
    username: str
    password: str

class GoodModel(BaseModel):
    goodname: str
    goodid: int
    quantity: int
   

@app.post("/register")
async def register(userdata: UserModel):
    """
    @brief Register User
    @param Userdata containing username and password
    @return Status message
    @throws HTTPException 500 if registering fails
    """
    try:
        print(f"DEBUG: User {userdata.username} trying to register")

        if market.getUser(userdata.username) != None:
            print(f"DEBUG: User {userdata.username} exists already")
            raise HTTPException(status_code=406, detail="User already registered or occupied username")
        
        market.registerUser(userdata.username, userdata.password)

        print(f"DEBUG: User {userdata.username} registered successfully")

        return {"message": f"{userdata.username} registered"}
    except Exception as e:
        print(f"ERROR registering: {e}")
        raise HTTPException(status_code=500, detail=f"Failed to register: {str(e)}")


@app.post("/login")
async def login(userdata: UserModel):
    """
    @brief Login User
    @param Userdata containing username and password
    @return Status message
    @throws HTTPException 500 if logging in fails
    """
    try:
        print(f"DEBUG: User {userdata.username} trying to login")

        if market.getUser(userdata.username) == None:
            print(f"DEBUG: User {userdata.username} not found")
            raise HTTPException(status_code=404, detail="User not found")
        
        # FIX: Verwendet market.loginUser statt user.authenticate
        if not market.loginUser(userdata.username, userdata.password):
            print(f"DEBUG: {userdata.password} is not the right password")
            raise HTTPException(status_code=400, detail="incorrect password")

        print(f"DEBUG: User {userdata.username} logged in successfully")

        return {"message": f"{userdata.username} logged in"}
    except Exception as e:
        print(f"ERROR logging in: {e}")
        raise HTTPException(status_code=500, detail=f"Failed to login: {str(e)}")
    

@app.get("/{username}/accountinfo")
async def accountinfo(username: str):
    """
    @brief Useraccount Info
    @param Username
    @return Balance and Inventory
    @throws HTTPException 500 if showing account fails
    """
    try:
        user = market.getUser(username)
        if user == None:
            print(f"DEBUG: {username} not found")
            raise HTTPException(status_code=404, detail="User not found")
        
        # FIX: Verwendet user-Objekt statt undefinierte Variablen
        balance = user.getAccount().getBalance()
        inventory = user.getInventory()
        
        # FIX: Erstelle Listen für alle Inventar-Items
        inventory_data = {
            "ID": [],
            "Name": [],
            "Price": [],
            "Quantity": []
        }
        
        for good_id, quantity in inventory.items():
            good = market.getGood(good_id)
            if good:
                inventory_data["ID"].append(good.getId())
                inventory_data["Name"].append(good.getName())
                inventory_data["Price"].append(good.getCurrentPrice())
                inventory_data["Quantity"].append(quantity)

        return {
            "balance": balance,
            "ID": inventory_data["ID"],
            "Name": inventory_data["Name"],
            "Price": inventory_data["Price"],
            "Quantity": inventory_data["Quantity"]
        }
    except Exception as e:
        print(f"ERROR showing account: {e}")
        raise HTTPException(status_code=500, detail=f"Failed to show Account: {str(e)}")


@app.get("/prices")
async def prices():
    """
    @brief Updating prices
    @return Updated prices
    @throws HTTPException 500 if prices updating fails
    """
    try:
        market.updatePrices()
        
        # FIX: Gebe aktuelle Preise zurück
        goods = market.getGoods()
        prices_data = {}
        for good in goods:
            prices_data[good.getId()] = good.getCurrentPrice()

        return {"prices": prices_data}
    except Exception as e:
        print(f"ERROR updating prices: {e}")
        raise HTTPException(status_code=500, detail=f"Failed to update prices: {str(e)}")
    

@app.get("/offers")
async def offers():
    """
    @brief Presents all goods
    @return All data from each good (ID, Name, Price, Quantity)
    @throws HTTPException 500 if showing goods fails
    """
    try:
        goods = market.getGoods()
        
        # FIX: Erstelle Listen für alle Güter-Daten
        goods_data = {
            "ID": [],
            "Name": [],
            "Price": [],
            "Quantity": []
        }
        
        for good in goods:
            goods_data["ID"].append(good.getId())
            goods_data["Name"].append(good.getName())
            goods_data["Price"].append(good.getCurrentPrice())
            goods_data["Quantity"].append(good.getQuantity())

        return goods_data
    except Exception as e:
        print(f"ERROR showing offers: {e}")
        raise HTTPException(status_code=500, detail=f"Failed to show offers: {str(e)}")


@app.post("/{password}/buy")
async def buy(password: str, data: GoodModel, userdata: UserModel):
    """
    @brief Buying goods
    @param Gooddata containing name and quantity
    @param Current Userdata
    @param Users password
    @return Inventory and Balance
    @throws HTTPException 500 if buying good fails
    """
    try:
        print(f"DEBUG: Trying to buy {data.goodname}")

        if market.getGood(data.goodid) == None:
            print("DEBUG: Good does not exist")
            raise HTTPException(status_code=404, detail="Good is not represented in the market")

        good = market.getGood(data.goodid)
        if data.quantity > good.getQuantity():
            print("DEBUG: Not enough goods left")
            raise HTTPException(status_code=400, detail="Not enough goods in the market left")

        # FIX: Verwende market.loginUser für Authentifizierung
        if not market.loginUser(userdata.username, userdata.password):
            print("DEBUG: Wrong password")
            raise HTTPException(status_code=406, detail="Incorrect password")

        user = market.getUser(userdata.username)
        price = good.getCurrentPrice()
        amount = price * data.quantity
        
        if not user.getAccount().hasEnoughBalance(amount):
            print("DEBUG: Not enough money")
            raise HTTPException(status_code=400, detail="Not enough money")
        
        # FIX: Verwende market.buyGood statt separate Funktionen
        if not market.buyGood(data.goodid, data.quantity):
            print("DEBUG: Buy transaction failed")
            raise HTTPException(status_code=500, detail="Buy transaction failed")

        # FIX: Aktualisiere Antwort-Format wie in accountinfo
        balance = user.getAccount().getBalance()
        inventory = user.getInventory()
        
        inventory_data = {
            "ID": [],
            "Name": [],
            "Price": [],
            "Quantity": []
        }
        
        for good_id, quantity in inventory.items():
            good_obj = market.getGood(good_id)
            if good_obj:
                inventory_data["ID"].append(good_obj.getId())
                inventory_data["Name"].append(good_obj.getName())
                inventory_data["Price"].append(good_obj.getCurrentPrice())
                inventory_data["Quantity"].append(quantity)

        return {
            "balance": balance,
            "ID": inventory_data["ID"],
            "Name": inventory_data["Name"],
            "Price": inventory_data["Price"],
            "Quantity": inventory_data["Quantity"]
        }
    except Exception as e:
        print(f"ERROR buying good: {e}")
        raise HTTPException(status_code=500, detail=f"Failed to buy good: {str(e)}")


@app.post("/{password}/sell")
async def sell(password: str, data: GoodModel, userdata: UserModel):
    """
    @brief Selling goods
    @param Gooddata containing name and quantity
    @param Current Userdata
    @param Users password
    @return Inventory and Balance
    @throws HTTPException 500 if selling good fails
    """
    try:
        print(f"DEBUG: Trying to sell {data.goodname}")

        if market.getGood(data.goodid) == None:
            print("DEBUG: Good does not exist")
            raise HTTPException(status_code=404, detail="Good is not represented in the market")

        # FIX: Verwende market.loginUser für Authentifizierung
        if not market.loginUser(userdata.username, userdata.password):
            print("DEBUG: Wrong password")
            raise HTTPException(status_code=406, detail="Incorrect password")

        user = market.getUser(userdata.username)
        user_quantity = user.getGoodQuantity(data.goodid)
        
        if data.quantity > user_quantity:
            print("DEBUG: Not enough in inventory")
            raise HTTPException(status_code=400, detail="Not enough goods in the inventory")

        # FIX: Verwende market.sellGood statt separate Funktionen
        if not market.sellGood(data.goodid, data.quantity):
            print("DEBUG: Sell transaction failed")
            raise HTTPException(status_code=500, detail="Sell transaction failed")

        # FIX: Gleiches Antwort-Format wie bei buy
        balance = user.getAccount().getBalance()
        inventory = user.getInventory()
        
        inventory_data = {
            "ID": [],
            "Name": [],
            "Price": [],
            "Quantity": []
        }
        
        for good_id, quantity in inventory.items():
            good_obj = market.getGood(good_id)
            if good_obj:
                inventory_data["ID"].append(good_obj.getId())
                inventory_data["Name"].append(good_obj.getName())
                inventory_data["Price"].append(good_obj.getCurrentPrice())
                inventory_data["Quantity"].append(quantity)

        return {
            "balance": balance,
            "ID": inventory_data["ID"],
            "Name": inventory_data["Name"],
            "Price": inventory_data["Price"],
            "Quantity": inventory_data["Quantity"]
        }
    except Exception as e:
        print(f"ERROR selling good: {e}")
        raise HTTPException(status_code=500, detail=f"Failed to sell good: {str(e)}")

@app.post("/logout")
async def logout(userdata: UserModel):
    """
    @brief Logging user out
    @param Current Userdata
    @return Status message
    @throws HTTPException 500 if logging out fails
    """
    try:       
        print(f"DEBUG: {userdata.username} trying to logout")

        # FIX: Verwende market.logout mit Passwort-Parameter
        if not market.logout(userdata.username, userdata.password):
            print("DEBUG: Logout failed")
            raise HTTPException(status_code=400, detail="Logout failed")

        return {"message":f"{userdata.username} logged out"}
    except Exception as e:
        print(f"ERROR logging out: {e}")
        raise HTTPException(status_code=500, detail=f"Failed to logout: {str(e)}")


if __name__ == '__main__':
    uvicorn.run("fastapi_server:app", host="127.0.0.1", port=8000, reload=True)