class Connection:
    initial_port = 55000
    conn_limit = 10
    conn_count = 0
    def __init__(self, some_host):
        self.host = some_host
        if Connection.conn_count < Connection.conn_limit:
            # self.port = Connection.initial_port + self.conn_count  # I think that I get the same results with :
            self.port = Connection.initial_port + Connection.conn_count
            Connection.conn_count += 1   
    def __repr__(self):
        return f"{self.host}, is using {self.port}"
    def close(self):
        Connection.conn_count -= 1 

class newConnection:
    initial_port = 55000
    conn_limit = 10
    conn_count = 0
    @classmethod
    def get_next_port(cls):
        return cls.initial_port + cls.conn_count
    @classmethod
    def get_connection_count(cls):
        return cls.conn_count
    @classmethod
    def add_connection(cls):
        cls.conn_count += 1
    @classmethod
    def remove_connection(cls):
        cls.conn_count -= 1
    def __init__(self, some_host):
        self.host = some_host
        if Connection.conn_count < Connection.conn_limit:
            self.port = self.get_next_port()
            self.add_connection()
    def __repr__(self):
        return f"{self.host}, is using {self.port}"
    def close(self):
        self.remove_connection()
        
print('Connection.__dict__ : \n', Connection.__dict__)
conn_instance00 = Connection('hostname00')
print("    After 1st instance :    ") 
print('Connection.__dict__ : \n', Connection.__dict__)
print('conn_instance00.__dict__ : \n', conn_instance00.__dict__)
conn_instance01 = Connection('hostname01')
print("    After 2nd instance :    ") 
print('Connection.__dict__ : \n', Connection.__dict__)
print('conn_instance01.__dict__ : \n', conn_instance01.__dict__)
conn_instance02 = Connection('hostname02')
print("    After 3rd instance :    ") 
print('Connection.__dict__ : \n', Connection.__dict__)
print('conn_instance02.__dict__ : \n', conn_instance02.__dict__)
print("  Lets see some more info after the 3rd instance:   " )
print("Connection.conn_count:", Connection.conn_count)
print(conn_instance00)
print(conn_instance01)
print(conn_instance02)
conn_instance00.close()
conn_instance01.close()
conn_instance02.close()
print("After closing connections:")
print('Connection.__dict__ : \n', Connection.__dict__)

print("\n\n  Lets use @classmethod:")
print('newConnection.__dict__ : \n', newConnection.__dict__)
conn_instance00 = newConnection('hostname00')
print("    After 1st instance :    ") 
print('newConnection.__dict__ : \n', newConnection.__dict__)
print('conn_instance00.__dict__ : \n', conn_instance00.__dict__)
conn_instance01 = newConnection('hostname01')
print("    After 2nd instance :    ") 
print('newConnection.__dict__ : \n', newConnection.__dict__)
print('conn_instance01.__dict__ : \n', conn_instance01.__dict__)
conn_instance02 = newConnection('hostname02')
print("    After 3rd instance :    ") 
print('Connection.__dict__ : \n', newConnection.__dict__)
print('conn_instance02.__dict__ : \n', conn_instance02.__dict__)
print("  Lets see some more info after the 3rd instance:   " )
print("Connection.conn_count:", newConnection.conn_count)
print(conn_instance00)
print(conn_instance01)
print(conn_instance02)
conn_instance00.close()
conn_instance01.close()
conn_instance02.close()
print("After closing connections:")
print('Connection.__dict__ : \n', newConnection.__dict__)

