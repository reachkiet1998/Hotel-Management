
def connector():
    from pymongo import MongoClient
    connection="mongodb+srv://bobbykiet168:FrDIj0zBtVUaRJxs@mycluster.fvdkll2.mongodb.net/?retryWrites=true&w=majority"

    client=MongoClient(connection)
    n=len(client.list_database_names())
    return client

client=connector()
db1=client["Hotel_Management"]
col_profile=db1["collection_profile"]


def printer(n):
    for i in range(len(n)):
        print((i+1),".", n[i])

def log_sign():
    n=["Login",
       "Sign Up",
       "Back"]
    printer(n)

def vaildator_user(col,user,pw,b):
    from pymongo import MongoClient
    a=[]
    z=col.find_one({"Username":str(user)})
    if z==None:
        print("Incorrect Please Try Again")
        while b>=0:
            if b==0:
                print("Please Signup")
                signup(col)
                login(col,b)
            else:
                b=b-1
                login(col,b)
    else:
        a.append(z["Username"])
        a.append(z["Password"])
        if a[0]==str(user) and a[1]==str(pw):
            print("Login Successful")
            return True
        else:
            print("Incorrect Please Try Again")
            while b>=0:
                if b==0:
                    print("Please Signup")
                    signup(col)
                    login(col,b)
                else:
                    b=b-1
                    login(col,b)

    

    

def login(collection,b):
    user=str(input("Please Input Username: "))
    pw=str(input("Please Input Password: "))
    a=vaildator_user(collection,user,pw,b-1)
    if a==True:
        c=accinfo()
        return c

def signup(n):
    from pymongo import MongoClient
    profile={}
    user=str(input("Please Create Username: "))
    profile["Username"]=user
    pw=str(input("Please Create Password: "))
    verify=str(input("Please Confirm Password: "))
    while pw!=verify:
        verify=str(input("Password Does not match please check again: "))
        if pw==verify:
            profile["Password"]=pw
            print(profile)
            n.insert_one(profile)

def accinfo():
    acc=["Your Account",
         "Room Management",
         "Hotel Booking",
         "Staff Management",
         "Exit"]
    
    printer(acc)
    a=(int(input("Please Choose one of the following: ")))
    return a

def home():
    option=["Login or Signup",
            "Room Management",
            "Hotel Booking",
            "Staff Management",
            "Exit"]

    printer(option)

def room_management(rom_col):
    option=["Show all Room",
            "Create Room",
            "Delete Room",
            "Update Room",
            "Back to Account"]
    printer(option)
    a=int(input("Please Choose one of the following: "))
    if a==1:
        show()
    if a==2:
        create_room(rom_col)
    if a==3:
        delete()
    if a==4:
        update()
    if a==5:
        accinfo()

def booking_info(book_col):
    option=["Show all Available Room",
            "Show all Unavailble Room",
            "Book a Room"
            "Back to Account"]
    printer(option)

def staff_management(staff_col):
    option=["Show all Staff",
            "Create Staff",
            "Delete Staff",
            "Update Staff",
            "Back to Account"]
    
    a=int(input("Please Choose one of the following: "))
    if a==1:
        show()
    if a==2:
        create_staff(staff_col)
    if a==3:
        delete()
    if a==4:
        update()
    if a==5:
        accinfo()

def cond_c(n,rom_col,book_col,staff_col):
    if n==2:
        room_management(rom_col)
    if n==3:
        booking_info(book_col)
    if n==4:
        staff_management(staff_col)

def show():
    pass

def create_staff(collection):
    from pymongo import MongoClient
    profile={}
    fn=str(input("Please Input First Name: "))
    profile["First Name"]=fn
    ln=str(input("Please Input Last Name: "))
    profile["Last Name"]=ln
    job_title=str((input("Please Input Job Title: ")))
    profile["Job Title"]=job_title
    emp_time=int(input("Please input employment time: "))
    profile["Employment Time"]=emp_time
    gender=str(input("Please input gender: "))
    profile["Gender"]=gender
    age=int(input("Please Input Age"))
    profile["Age"]=age
    address=str(input("Please input address: "))
    profile["Address"]=address
    email=str(input("Please input email: "))
    profile["Email"]=email
    number=str(input("Please input phnoe number: "))
    profile["Phnon Number"]=number

    collection.insert_one(profile)

def create_room(collection):
    from pymongo import MongoClient
    profile={}
    room_name=str(input("Please Input Room Name: "))
    profile["Room Name"]=room_name
    room_floor=str(input("Please Input Room Floor: "))
    profile["Room Floor"]=room_floor
    beds=str(input("Please Input Number of Beds: "))
    profile["Bed Numbers"]=beds
    room_type=str(input("Please Input Room Type: "))
    profile["Room Type"]=room_type    
    room_status=str(input("Please Input Room Status: "))
    profile["Room Status"]=room_status
    collection.insert_one(profile)

def delete():
    pass

def update():
    pass

def available():
    pass

def unavailble():
    pass