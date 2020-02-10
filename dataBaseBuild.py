from datetime import datetime
studentId = str(input("Enter your ID here: ")) #students input there student id numbers
now = str(datetime.now())
if studentId in ("110255","112266","123987","212901"): #this is my database of students
    print("Come on In!!") # if student belongs GOOD
else:
    print("Get out of here!!") # if student does not belong BAD
    myFile= open("guru99.txt","w+")
    
    for i in range(1):
        myFile.write("Admin. Notified Student entered: " + studentId + now)
        
        # Returns a datetime object containing the local date and time
        
''' How can we notify admin about a student in the wrong class'''

