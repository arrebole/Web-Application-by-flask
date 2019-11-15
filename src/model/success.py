def LoginSuccess(cookie: str):
    return {
        "code": 0,
        "message": "login success",
        "data":{
            "cookie": cookie
        }
    }