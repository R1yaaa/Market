from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
from typing import List, Dict, Optional
import uvicorn
import uuid
import unolib
from unolib import Market, Account, User, Good

app = FastAPI()

class UserModel(BaseModel):
    username: str
    password: str

class GoodModel(BaseModel):
    goodname: str
    quantity: int
   

@app.post("/register")
async def register(user: UserModel):
    """
    @brief Register User
    @param Userdata containing username and password
    @return Status message
    @throws HTTPException 500 if registering fails
    """
    try:
        print(f"DEBUG: User {user.username} trying to register")

        if market.getUser(user.username) != None:
            print(f"DEBUG: User {user.username} exists already")
            raise HTTPException(status_code=406, detail="User already registered or occupied username")
        
        market.registerUser(user.username, user.password)

        print(f"DEBUG: User {user.username} registered successfully")

        return {"message": f"{user.username} registered"}
    except Exception as e:
        print(f"ERROR registering: {e}")
        raise HTTPException(status_code=500, detail=f"Failed to register: {str(e)}")


@app.post("/login")
async def login(data: UserModel):
    """
    @brief Login User
    @param Userdata containing username and password
    @return Status message
    @throws HTTPException 500 if logging in fails
    """
    try:
        print(f"DEBUG: User {data.username} trying to login")

        if market.getUser(data.username) == None:
            print(f"DEBUG: User {data.username} not found")
            raise HTTPException(status_code=404, detail="User not found")
        
        if not user.authenticate(data.username, data.password): #in hpp ohne username parameter
            print(f"DEBUG: {data.password} is not the right password")
            raise HTTPException(status_code=400, detail="incorrect password")
        
        market.loginUser(data.username, data.password)

        print(f"DEBUG: User {data.username} logged in successfully")

        return {"message": f"{data.username} logged in"}
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
        if market.getUser(username) == None:
            print(f"DEBUG: {username} not found")
            raise HTTPException(status_code=404, detail="User not found")
        
        balance = account.getBalance(username)  #kein parameter in hpp
        inventory = user.getInventory(username) #kein parameter in hpp

        return {
            "balance": balance,
            "inventory": inventory
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
        prices = market.updatePrices()

        return {"prices": prices}
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
        obj_goods = market.getGoods()

        return {
            "ID": obj_goods.getId,
            "Name": obj_goods.getName,
            "Price": obj_goods.getPrice,
            "Quantity": obj_goods.getQuantity
        }
    except Exception as e:
        print(f"ERROR showing offers: {e}")
        raise HTTPException(status_code=500, detail=f"Failed to show offers: {str(e)}")


@app.post("/{password}/buy")
async def buy(data: GoodModel, request: Request, password: str):
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

        username = request.headers.get("username")

        goodId = good.getId(data.goodname)    #in hpp ohne parameter
        if market.getGood(goodId) == None:
            print("DEBUG: Good does not exist")
            raise HTTPException(status_code=404, detail="Good is not represented in the market")

        restquantity = good.getQuantity(goodId) #in hpp ohne parameter
        if data.quantity > restquantity:
            print("DEBUG: Not enough goods left")
            raise HTTPException(status_code=400, detail="Not enough goods in the market left")

        if not user.authenticate(username, password):    #in hpp ohne username parameter
            print("DEBUG: Wrong password")
            raise HTTPException(status_code=406, detail="Incorrect password")

        price = good.getCurrentPrice(goodId)    #in hpp ohne parameter
        amount = price*data.quantity
        if not account.hasEnoughBalance(username, amount):  #in hpp ohne username parameter
            print("DEBUG: Not enough money")
            raise HTTPException(status_code=400, detail="Not enough money")
        
        market.buyGood(username, goodId, data.quantity) #in hpp ohne username parameter

        balance = account.getBalance(username)  #in hpp ohne parameter
        inventory = user.getInventory(username) #in hpp ohne parameter

        return {
            "inventory":inventory,
            "balance":balance
        }
    except Exception as e:
        print(f"ERROR buying good: {e}")
        raise HTTPException(status_code=500, detail=f"Failed to buy good: {str(e)}")


@app.post("/{password}/sell")
async def sell(data: GoodModel, request: Request, password: str):
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

        username = request.headers.get("username")

        goodId = good.getId(data.goodname)    #in hpp ohne parameter
        if market.getGood(data.goodId) == None:
            print("DEBUG: Good does not exist")
            raise HTTPException(status_code=404, detail="Good is not represented in the market")

        if not user.authenticate(username, password):   #in hpp ohne username parameter
            print("DEBUG: Wrong password")
            raise HTTPException(status_code=406, detail="Incorrect password")

        anzahl = user.getGoodQuantity(username, goodId) #in hpp ohne username parameter
        if data.quantity > anzahl:
            print("DEBUG: Not enough in inventory")
            raise HTTPException(status_code=400, detail="Not enough goods in the inventory")

        market.sellGood(username, goodId, data.quantity)    #in hpp ohne username parameter

        balance = account.getBalance(username)  #in hpp ohne parameter
        inventory = user.getInventory(username) #in hpp ohne parameter

        return {
                "inventory":inventory,
                "balance":balance
            }
    except Exception as e:
        print(f"ERROR selling good: {e}")
        raise HTTPException(status_code=500, detail=f"Failed to sell good: {str(e)}")

@app.post("/logout")
async def logout(request: Request):
    """
    @brief Logging user out
    @param Current Userdata
    @return Status message
    @throws HTTPException 500 if logging out fails
    """
    try:
        username = request.headers.get("username")        
        print(f"DEBUG: {username} trying to logout")

        market.logout(username) #in hpp ohne parameter

        return {"message":f"{username} logged out"}
    except Exception as e:
        print(f"ERROR logging out: {e}")
        raise HTTPException(status_code=500, detail=f"Failed to logout: {str(e)}")
    
#request?


if __name__ == '__main__':
    uvicorn.run("fastapi_server:app", host="127.0.0.1", port=8000, reload=True)
