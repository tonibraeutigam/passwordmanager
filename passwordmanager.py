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
            if not exists(exist_file_name):
                print("File is not existing")
            else:
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
    exist_file_name = str(input("Enter the name of the databank you want to use: "))
    
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
        elif choice == "2":
            add_new_password(exist_file_name)
        elif choice == "3":
            line_number = int(input("Which linie do you want to delete: "))    
            delete_existing_password(exist_file_name, line_number) 
        elif choice == "4":
            line_number = int(input("In which line do you want to change the password: "))
            update_password(exist_file_name, line_number)
        elif choice == "5":
            exit = True
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
   

def add_new_password(file_name):
    f = open(file_name, "a") #append1
    name = (str(input("Please enter your name:")))
    password = (str(input("Please enter your password:")))
    url = (str(input("Please enter your URL:")))
    note = (str(input("Please enter your Note:")))
    pw_data = f.write(str(name + ";" + password + ";" + url + ";" + note + "\n"))
    f.close()
    

def delete_existing_password(exist_file_name, line_number):
    
    with open(exist_file_name) as file:
        # reading line by line
        lines = file.readlines()
        
    if(line_number <=len(lines)):
        del lines[line_number -1]
        
        with open(exist_file_name, "w") as file:
            for line in lines:
                file.write(line)
    else:
        print("Line", line_number, " not in file.")
        print("File has", len(lines), "lines.")

def update_password(exist_file_name, line_number):

    with open(exist_file_name) as file:
        # reading line by line
        lines = file.readlines()
        #print(lines)
        
    if(line_number <=len(lines)):
        new_password = input("Enter your new Password: ")
        data = lines[line_number -1].strip().split(';')
        data[1] = new_password
        lines[line_number - 1] = (data[0] + ";" + data[1] + ";" + data[2] + ";" + data[3] + "\n")
        
        with open(exist_file_name, "w") as file:
            for line in lines:
                file.write(line)
    else:
        print("Line", line_number, " not in file.")
        print("File has", len(lines), "lines.")
        
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
#delete_existing_password("test.txt", 2)
