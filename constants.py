from sqlalchemy import create_engine


class ConnectDatabase():
    def __init__(self) -> None:
        self._databse_url = None
        self._session = None

    @property
    def databse_url(self):
        if self._databse_url == None:
            user = 'avnadmin'
            password = 'AVNS_g4ffSjirusDWXF9IJy1'
            host = 'mysql-30e7473a-afsheenzaahrah25-614f.i.aivencloud.com:23263'
            database = 'demo'
            DATABASE_URL_FORMAT = f'mysql+mysqlconnector://{user}:{password}@{host}/{database}'
            self._databse_url = DATABASE_URL_FORMAT
            return self._databse_url
        else:
            return self._databse_url
    
    @property
    def make_session(self):
        if self._session == None:
            self._session = create_engine(self.databse_url)
            return self._session
        else:
            return self._session

# if __name__ == "__main__":
#     db = ConnectDatabase()
#     print("Connecting to database")
#     session = db.make_session
#     print("Session created successfully:", session)