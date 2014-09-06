class User:
    def __init__(self, access_token, _id, expires_in):
        self._access_token = access_token
        self._id = _id
        self._expires_in = expires_in

    @property
    def access_token(self):
        return self._access_token

    @property
    def user_id(self):
        return self._id
    
    @property
    def expires_in(self):
        return self._expires_in
