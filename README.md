# Finantier

This project contains three services: auth, main, and encrypt service

The main service receives a request to get data for a particular stock symbol.

The main service fetches the data and sends it to the encrypt service to get that data in encrypted form

Then the main service returns the encrypted data back as a response.

Both the services validates the token present in the request 

### Steps to run the application
Clone the repo from -> ```https://github.com/gy2108/finantier.git```

```cd finantier```

```docker-compose up```

### Services
#### 1.  auth
Endpoint: ```/token/{user_id}```

Sample Request: ```http://localhost:8001/token/101```

Sample Response: ```{
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxMDEsImV4cCI6MTYyMjk5OTg1Mn0.Vn3cd158_IrNWOelYQI33eh4odDXWbMW6HIpgzJJ1Rs"
        }```
        
#### 2. main
Endpoint: ```/symbol/{symbol}```

Sample Request: ```http://localhost:8002/symbol/INFY```


Sample Response: ```{
    "cipher_text": "gWr2pdc7BAhPlYid27ATTSeiUYdhjzQcMOjbD5FP0RcgNUZqPz6DHHeWPzwq0dLGWmXMA8eiuQ=="
}```

If token exired: ```{
    "message": "token is invalid"
}```

If token not passed: ```{
    "message": "a valid token is missing"
}```


#### 3. encrypt
Endpoint: ```/encrypt```, Request Body: Json 

Sample Request: ```http://localhost:8003/encrypt```

Request Body : ```{
        "symbol": "IBM",
        "open": "146.0000",
        "high": "147.5500",
        "low": "145.7600",
        "price": "147.4200",
        "volume": "3117905",
        "latest trading day": "2021-06-04",
        "previous close": "145.5500",
        "change": "1.8700",
        "change percent": "1.2848%"
    }```
    
Sample Response: ```{
    "cipher_text": "/+R7b//f9m/DAnLlDsXxjs+5TRIgb5bwZAGbqyzop0wKB5KOFEZHzcXeD8cE3rW/DdOjP9qHbz8F8SlN2NuVw=="
}```

If token not passed: ```{
    "message": "a valid token is missing"
}```

If token expired: ```{
    "message": "token is invalid"
}```


Currently the Auth service is only working as per the expiry time of the token(30 seconds)
Would have implemented database service to store few users to validate the userid from the decoded token, but was not able to do because of time constraint.
So for now the service gives back proper response till the time token is valid, doesn't depend which user is making the request.