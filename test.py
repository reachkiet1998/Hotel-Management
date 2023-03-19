from classes import *
client=connector()
db1=client["Hotel_Management"]
col_booking=db1["collection_booking"]
col_profile=db1["collection_profile"]
col_room=db1["collection_room"]
col_staff=db1["collection_staff"]

a=col_room.find_one({"Room Name":"BOBBY VIP ROOM"})

print(a)