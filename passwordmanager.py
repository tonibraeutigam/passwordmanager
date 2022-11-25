from os.path import exists
import glob


def main():
    exit = False 
    while exit == False:
        choice = mainmenu()
        if choice == "1":
            filename = create_database()
            #print(filename)
            mainmenu_two(filename)
        elif choice == "2":
            open_database()
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
    open_file = str(input("tip down the name of the databank you want to use: "))

    f = open(open_file, "r") #read
    for line in f: 
        print(line.rstrip()) # rstrip entfernt Leerzeichen und Zeilenumbruche vom rechten Ende der Zeile
    f.close()

def mainmenu_two(file_name):
    
    exit = False 
    while exit == False:    
        print("===========================================")
        print("             Passwordmaganager " + str(file_name))
        print("===========================================")
        print(" 1) Show existing passwords")
        print(" 2) Add new password ")
        print(" 3) Delete an existing password")
        print(" 4) Update password")
        print(" 5) Exit")
        
        choice = str(input("What do you like to do?: "))

        if choice == "1":
            filename = show_existing_password(file_name)
            #print(filename)
            #doc_header()
            mainmenu_two(file_name)
        elif choice == "2":
            add_new_password(file_name)
        elif choice == "3":
            delete_existing_password()
        elif choice == "4":
            update_password()
        elif choice == "5":
            exit == True
        else:
            print ("Invalid Input")

def show_existing_password(file_name):
    f = open(file_name, "r") #read
    for line in f: 
        print(line.rstrip()) # rstrip entfernt Leerzeichen und Zeilenumbruche vom rechten Ende der Zeile
        f.close()
        return file_name
    #Daten müssen formatiert angezeigt werden 

def add_new_password(file_name):
    f = open(file_name, "a") #append
    name = (str(input("Please enter your name:")))
    password = (str(input("Please enter your password:")))
    url = (str(input("Please enter your URL:")))
    note = (str(input("Please enter your Note:")))
    pw_data = f.write(str(name + ":" + password + ":" + url + ":" + note))
    f.close()
    #4x Input + Text Name?, Password?, Url?, Note?
    #zusammenfassen in einen Variable(String) 
    #mit append f = open(file_name, "a") #append
    #f.write(str() + "\n") //hier wird der String(Variable) hinzugefügt
    #f.close()
    return pw_data

def delete_existing_password():
    pass

def update_password():
    pass

def doc_header():
    print("--------------------------------------------------------------------------------------")
    header = "{0:10s}{1:10s}{2:25s}{3:30s}{4:50s}".format("Index","Name","Password","URL","Note")
    print("--------------------------------------------------------------------------------------")
    return header



#print (doc_header())
main()
#open_database()
