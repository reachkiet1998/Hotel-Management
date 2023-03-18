from classes import *
client=connector()
if len(client.list_database_names())>0:
    print("Connection Successful")
    db1=client["Hotel_Management"]
    col_booking=db1["collection_booking"]
    col_profile=db1["collection_profile"]
    col_room=db1["collection_room"]
    col_staff=db1["collection_staff"]
    while True:
        home()
        
        a=int(input("Please Choose one of the following: "))

        if a==5:
            break
        if a==1:
            log_sign()
            b=int(input("Please Choose one of the following: "))
            if b==1:
                c=login(col_profile,4)
                if c==5:
                        break
                else:
                        cond_c(c,col_room,col_booking,col_staff)
            
            if b==2:
                signup(col_profile)
                c=login(col_profile,4)
                if c==5:
                        break
                else:
                        cond_c(c,col_room,col_booking,col_staff)
        else:
            option=["Login or Signup",
                    "Exit"]
            printer(option)
            a=int(input("Please Choose one of the following: "))
            if a==2:
                break
            else:
                log_sign()
                a=int(input("Please Choose one of the following: "))
                if a==1:
                    login(col_profile,4)
                    a=(int(input("Please Choose one of the following: ")))
                    if a==5:
                        break
                    else:
                        cond_c(a,col_room,col_booking,col_staff)
                if a==2:
                    signup(col_profile)
                    login(col_profile,4)
                    a=(int(input("Please Choose one of the following: ")))
                    if a==5:
                        break
                    else:
                        cond_c(a,col_room,col_booking,col_staff)
                    