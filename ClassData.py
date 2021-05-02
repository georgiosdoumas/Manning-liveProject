class Connection:
    initial_port = 55000
    conn_limit = 10
    conn_count = 0
    def __init__(self, some_host):
        # set the host for the instance
        self.host = some_host
        # set the port based on the class variable port
        self.port = self.initial_port + self.conn_count
        # add 1 to the class's connection_count
        self.conn_count += 1
    def __repr__(self):
        return f"{self.host}, is using {self.port}"
    def close(self):
        # reduce the class's connection_count by 1
        self.conn_count -= 1 

class listConnection:
    start_port = 55000
    conn_limit = 10
    connections = []
    def __init__(self, some_host):
        if len(self.connections) == self.conn_limit:
            print(" ERROR! You cannot open a new connection, close one of the existing first")
            return
        self.host = some_host
        self.port = self.start_port + len(self.connections)
        self.connections.append(self)
    def close(self):
        self.connections.remove(self)
    def __repr__(self):
        return f"{self.host}, {self.port}"

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
# So we could not actually change the class attributes. 
print('    \n\n with the listConnection class, we have good results : ')
print('listConnection.__dict__ : \n', listConnection.__dict__)
conn_instance10 = listConnection('hostname10')
print("    After 1st instance :    ") 
print('listConnection.__dict__ : \n', listConnection.__dict__)
print('conn_instance10.__dict__ : \n', conn_instance10.__dict__)
conn_instance11 = listConnection('hostname11')
print("    After 2nd instance :    ") 
print('listConnection.__dict__ : \n', listConnection.__dict__)
print('conn_instance11.__dict__ : \n', conn_instance11.__dict__)
conn_instance12 = listConnection('hostname12')
print("    After 3rd instance :    ") 
print('listConnection.__dict__ : \n', listConnection.__dict__)
print('conn_instance12.__dict__ : \n', conn_instance12.__dict__)
print("  Lets see some more info after the 3rd instance:   " )
print("listConnection.connections:", listConnection.connections)
print(conn_instance10)
print(conn_instance11)
print(conn_instance12)
conn_instance10.close()
conn_instance11.close()
conn_instance12.close()
print("----- After closing all connections:")
print('listConnection.__dict__ : \n', listConnection.__dict__)
