class Database:

    def connect():
        pass

    def commit():
        pass

class MysqlDb:

    def connect_mysql(self):
        print('MySQL connection')

    def commit_mysql(self):
        print('MySQL commit')

class PostgresDb:

    def connect_postgres(self):
        print('PostgresSQL connection')

    def commit_postgres(self):
        print('PostgresSQL commit')

class MysqlDbAdapter(Database, MysqlDb):

    def connect(self):
        self.connect_mysql()

    def commit(self):
        self.commit_mysql()

class PostgresDbAdapter(Database, PostgresDb):

    def connect(self):
        self.connect_postgres()

    def commit(self):
        self.commit_postgres()

adapter = MysqlDbAdapter() # PostgresDbAdapter()

# main interface will not be chaged
adapter.connect() # MySQL connection
adapter.commit() # MySQL commit

