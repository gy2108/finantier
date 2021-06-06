# Finantier

This project contains three services: auth, main, and encrypt service

The main service receives a request to get data for a particular stock symbol.

The main service fetches the data and sends it to the encrypt(with AES 256) service to get that data in encrypted form

Then the main service returns the encrypted data back as a response.

Both the services validates the token present in the request 

For this project I have used ```https://www.alphavantage.co/documentation/``` as public API for fetching the stock symbol data
which has limitations like ```5 requests per 30 seconds and 500 requests per day```. I have hardcoded my apikey(free account).

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

```http code: 200```
        
#### 2. main
**Endpoint**: ```/symbol/{symbol}```

**Sample Request**: ```http://localhost:8002/symbol/INFY```


**Sample Response**: ```{
    "cipher_text": "gWr2pdc7BAhPlYid27ATTSeiUYdhjzQcMOjbD5FP0RcgNUZqPz6DHHeWPzwq0dLGWmXMA8eiuQ=="
}   http code : 200```

**If rate limit exceeded or error from public API** ```{"error_message": "Please try after Some time"} http code: 500```

**If symbol is invalid**: ```{"error_message": "Not a Valid Symbol"} http code : 404```

**If token exired**: ```{
    "error_message": "token is invalid"
}  http code : 403```

**If token not passed**: ```{
    "error_message": "a valid token is missing"
} http code : 403```


#### 3. encrypt
**Endpoint**: ```/encrypt```, Request Body: Json 

**Sample Request**: ```http://localhost:8003/encrypt```

**Request Body** : ```{
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
    
**Sample Response**: ```{
    "cipher_text": "/+R7b//f9m/DAnLlDsXxjs+5TRIgb5bwZAGbqyzop0wKB5KOFEZHzcXeD8cE3rW/DdOjP9qHbz8F8SlN2NuVw=="
} http code : 200```

**If token not passed**: ```{
    "error_message": "a valid token is missing"
} http code : 403```

**If token expired**: ```{
    "error_message": "token is invalid"
} http code : 403```


Currently the Auth service is only working as per the expiry time of the token(30 seconds)
Would have implemented database service to store few users to validate the userid from the decoded token, but was not able to do because of time constraint.
So for now the service gives back proper response till the time token is valid, doesn't depend which user is making the request.