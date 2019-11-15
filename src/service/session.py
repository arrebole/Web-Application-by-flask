# this is session module, Used for login sessions

import os, time, random, string

class User:
    def __init__(self, userName, password):
        self._userName = userName
        self._password = password
        self._sessionID = ""
        self._expires = 0.0

    def userName(self):
        return self._userName

    def passWord(self):
        return self._password
    
    def sessionID(self):
        return self._sessionID

    def extend(self):
        self._expires = time.time() + 60 *30
        self._sessionID = self.ranstr(30)

    def isExpires(self):
        if time.time() > self._expires:
            return True
        return False

    def ranstr(self, num):
        salt = ''.join(random.sample(string.ascii_letters + string.digits, num))
        return salt


class Store:
    def __init__(self):
        self._users = set()

    def registered(self, user: User):
        if user not in self._users:
            self._users.add(user)

    def login(self, userName: str, passWord: str)->str:
        for user in self._users:
            if user.userName() == userName and user.passWord() == passWord:
                if user.isExpires():
                    user.extend()
                return user.sessionID()
        return ""

    def isLogin(self, sessionID):
        for user in self._users:
            if user.sessionID() == sessionID and not user.isExpires():
                return True
            return False

sessionStore = Store()
sessionStore.registered(User(userName="root", password=os.environ.get("PASSWD", "dev")))