from os.path import exists
import glob

def main():
    exit = False 
    while exit == False:
        choice = mainmenu()
        if choice == "1":
            filename = create_database()
            mainmenu_two(filename)
        elif choice == "2":
            exist_file_name = open_database()
            mainmenu_two(exist_file_name)
        elif choice == "3":
            exit = True
        else:
            print ("Invalid Input")
    
def mainmenu():
    print("===========================================")
    print("             Passwordmaganager"             )
    print("===========================================")
    print("1) Create a new password database")
    print("2) Start with an existing database")
    print("3) cancel")
    2
    return str(input("What do you want to do ?: "))

def create_database():
    file_name = str(input("Please enter the name of the Database you want create: ")) + ".txt"
    if not exists(file_name):
        f = open(file_name, "w")
        f.close()
        return file_name

def open_database():
    txtfiles = []
    for file in glob.glob("*.txt"):
        txtfiles.append(file)
    print(txtfiles)
    exist_file_name = str(input("tip down the name of the databank you want to use: "))
    #if not exist ? 
    return exist_file_name
    

def mainmenu_two(exist_file_name): 
    exit = False 
    while exit == False:    
        print("===========================================")
        print("             Passwordmaganager " + str(exist_file_name))
        print("===========================================")
        print(" 1) Show existing passwords")
        print(" 2) Add new password ")
        print(" 3) Delete an existing password")
        print(" 4) Update password")
        print(" 5) Exit")
        
        choice = str(input("What do you like to do?: "))

        if choice == "1":
            show_existing_password(exist_file_name)
            mainmenu_two(exist_file_name)
        elif choice == "2":
            add_new_password(exist_file_name)
        elif choice == "3":
            delete_existing_password()
        elif choice == "4":
            update_password()
        elif choice == "5":
            exit == True
        else:
            print ("Invalid Input")

def show_existing_password(exist_file_name):
    doc_header()
    f = open(exist_file_name,'r')
    count = 0 
    for line in f:
        count += 1 
        data = line.strip().split(';')
        data_format = "{0:10s}{1:10s}{2:25s}{3:30s}{4:50s}".format(str(count),data[0],data[1],data[2],data[3])
        print(data_format)
    f.close()

        #data_format = "{0:10s}{1:10s}{2:25s}{3:320s}{4:50s}".format("index",data[0],data[1],data[2],data[3])
        #print(data_format)
        #return exist_file_name
   

def add_new_password(file_name):
    f = open(file_name, "a") #append1
    name = (str(input("Please enter your name:")))
    password = (str(input("Please enter your password:")))
    url = (str(input("Please enter your URL:")))
    note = (str(input("Please enter your Note:")))
    pw_data = f.write(str(name + ";" + password + ";" + url + ";" + note + "\n"))
    f.close()
    return file_name

def delete_existing_password():
    pass

def update_password():
    pass

def doc_header():
    print("--------------------------------------------------------------------------------------")
    header = "{0:10s}{1:10s}{2:25s}{3:30s}{4:50s}".format("Index","Name","Password","URL","Note")
    print(header)
    print("--------------------------------------------------------------------------------------")
    return header



#(doc_header())
main()
#open_database()
#show_existing_password()