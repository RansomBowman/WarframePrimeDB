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
        return print("{:<20s}{:<15s}{:<10s}{:<10s}{:<10s}".format(\
            self.name, self.wType,self.mast, self.vault, self.comp))
        ##return print(str(self.name + " " + self.wType.rjust(10) + " " + self.mast + " " + self.vault
          ##         + " " +  self.comp)) ##Use frmt alignment stuff
    
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
    print("6: Other Prime List")
    print("7: Add Prime to List")
    print("8: Edit Already Existing Entry")
    print("9: Print Mastered")
    print("10: Print Unmastered")
    print("-1: Exit")

def menu_input(cmd, objs):
    if cmd == 1:
        print_all(objs)
    elif cmd == 2:
        categ = 'Warframe'
        type_print(objs, categ)
    elif cmd == 3:
        categ = 'Primary'
        type_print(objs, categ)
    elif cmd == 4:
        categ = 'Secondary'
        type_print(objs, categ)
    elif cmd == 5:
        categ = 'Melee'
        type_print(objs, categ)
    elif cmd == 6:
        categ = 'Other'
        type_print(objs, categ)
    elif cmd == 7:
        pass
    elif cmd == 8:
        pass
    elif cmd == 9:
        pass
    elif cmd == 10:
        pass

def print_header():
    print("-" * 75)
    print("{:<20s}{:<15s}{:<10s}{:<10s}{:<10s}".format(\
        "Name", "Type", "Mastered", "Vaulted", "Components"))
    print("-" * 75)
    
def print_all(data):
    print()
    print("{:-^75}".format(" Commplete Prime List "))
    print_header()
    for i in range(len(data)):
        data[i].print_str() ##use align, call string func for indiv. data
    print()

def type_print(data, categ):
    print()
    print("{:-^75s}".format(" Commplete Prime {:s} List ".format(categ)))
    print_header()
    for i in range(len(data)):
        print
        if(data[i].get_wType()) == categ:
            data[i].print_str()
    print()


def sortItems(data):
    sortItemsAlpha(data)
    sortItemsType(data)


def sortItemsType(data):
    for i in range(len(data) - 1):
        if data[i][1] > data[i+1][1]:
            temp = data[i]
            data[i] = data[i+1]
            data[i+1] = temp
            sortItemsType(data)
            
def sortItemsAlpha(data):
    for i in range(len(data) - 1):
        if data[i][0] > data[i+1][0]:
            temp = data[i]
            data[i] = data[i+1]
            data[i+1] = temp
            sortItemsAlpha(data)

def main():
    f = open("weap_data.txt", 'r+')

    data = f.read()

    data = data.split("\n")
##    print(data)

    for n in range(len(data)):
        data[n] = data[n].split(",")

    sortItems(data)

    list_of_w = []
    
    for i in range(len(data)): ##check object class
        newW = Weapon(data[i][0], data[i][1], data[i][2], data[i][3], data[i][4])
        list_of_w.append(newW)
    
    userCMD = 0
    while userCMD != -1:
        print_menu()
        userCMD = int(input("Input desired option: "))
        menu_input(userCMD, list_of_w)
    
    ##print(list_of_w[0].getName())

    f.close()

main()
