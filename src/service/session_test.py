from service import sessionStore

def TestSession():
    if sessionStore.isLogin(""):
        print("test FAIL")
        exit(0)
   
    cookie = sessionStore.login("root", "dev")
    if not sessionStore.isLogin(cookie):
        print("test Fail")
        exit(0)