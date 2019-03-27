import string

class Weapon:
    """General Weapons and Warframes"""
    def __init__(self, name, wType, mastered, vaulted, comp):
        self.name = name
        self.wType = wType
        self.mast = mastered
        self.vault = vaulted
        self.comp = comp

    def print_str(self):
        return print(str(self.name + " " + self.wType + " " + self.mast + " " + self.vault
                   + " " +  self.comp)) ##Use frmt alignment stuff
    
    def statList(self):
        return self.name, self.wType, self.mast, self.vault, self.comp
    
    def setName(self, name):
        self.name = name
    def getName(self):
        return self.name

    def set_wType(self, wType):
        self.wType = wType
    def get_wType(self):
        return self.wType

    def setMast(self, mast):
        self.mast = mast
    def getMast(self):
        return self.mast

    def setVault(self, vault):
        self.vault = vault
    def getVault(self):
        return self.vault

    def setComp(self, comp):
        self.comp = comp
    def getComp(self):
        return self.comp
    
class Primary(Weapon):
    pass

class Secondary(Weapon):
    pass

class Melee(Weapon):
    pass

class Other(Weapon):
    pass

def print_menu():
    print("1: Complete Prime List")
    print("2: Warframe Prime List")
    print("3: Primary Prime List")
    print("4: Secondary Prime List")
    print("5: Melee Prime List")
    print("6: Add Prime to List")
    print("7: Edit Already Existing Entry")
    print("8: Print Mastered")
    print("9: Print Unmastered")
    print("-1: Exit")

def menu_input(cmd, objs):
    if cmd == 1:
        print_all(objs)
    elif cmd == 2:
        warfr_print(objs)
    elif cmd == 3:
        pass
    elif cmd == 4:
        pass
    elif cmd == 5:
        pass    
    elif cmd == 6:
        pass
    elif cmd == 7:
        pass
    elif cmd == 8:
        pass
    elif cmd == 9:
        pass

def print_header():
    pass

def print_all(data):
    print()
    print("--------Commplete Prime List--------")
    for i in range(len(data)):
        data[i].print_str() ##use align, call string func for indiv. data
    print()

def warfr_print(data):
    print()
    print("--------Commplete Prime Warframe List--------")
    for i in range(len(data)):
        print
        if(data[i].get_wType()) == 'Warframe':
            data[i].print_str()
    print()




def sortItems(data):
    pass

def main():
    f = open("weap_data.txt", 'r+')

    data = f.read()

    data = data.split("\n")
##    print(data)

    for n in range(len(data)):
        data[n] = data[n].split(",")
        
    list_of_w = []

    for i in range(len(data)): ##check object class
        newW = Weapon(data[i][0], data[i][1], data[i][2], data[i][3], data[i][4])
        list_of_w.append(newW)

    sortItems(list_of_w)
    
    userCMD = 0
    while userCMD != -1:
        print_menu()
        userCMD = int(input("Input desired option: "))
        menu_input(userCMD, list_of_w)
    
    ##print(list_of_w[0].getName())

    f.close()

main()
