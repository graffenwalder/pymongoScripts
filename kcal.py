import pymongo

##### Uncomment this part, if your running on a gnome-terminal ########
##### It launches mongod in a new terminal.                    ########
# import subprocess
# import time
#
# subprocess.call(['gnome-terminal', '--', 'mongod'])
# print("Wait 2 seconds for mongod to start up.....")
# time.sleep(2)
#######################################################################


myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["foodDB"]
mycol = mydb["fooditems"]


def showCollections():
    print(mydb.list_collection_names())
    emptyLines()


def showAll(mycol=mycol):
    for x in mycol.find():
        print(x)
    emptyLines()


def insertOne():
    name = input("Product Name: ")
    while True:
        try:
            kcal = float(input("Kcal :"))
            break
        except ValueError:
            print("Oops! That was not a valid number. Try again...")
            emptyLines(1)
    food = {"name": name, "kcal": kcal}
    x = mycol.insert_one(food)
    emptyLines(1)
    print("Succesfully added :", food)
    emptyLines()


def querySomething():
    myquery = {"kcal": {"$gt": 50}}
    mydoc = mycol.find(myquery)
    for x in mydoc:
        print(x)
    emptyLines()


def sortByName():
    mydoc = mycol.find().sort("name")
    for x in mydoc:
        print(x)
    emptyLines()


def sortByKcal():
    mydoc = mycol.find().sort("kcal", -1)  # , -1 after name = reverse
    for x in mydoc:
        print(x)
    emptyLines()


def deleteOne():
    name = input("Delete product: ")
    myquery = {"name": name}
    if mycol.find_one(myquery):
        mycol.delete_one(myquery)
        emptyLines(1)
        print("Succesfully deleted: " + name)
    else:
        emptyLines(1)
        print(name + " not found.")
    emptyLines()


def updateKcal():
    name = input("Product Name: ")
    myquery = {"name": name}
    if mycol.find_one(myquery):
        while True:
            try:
                kcal = float(input("Update Kcal :"))
                break
            except ValueError:
                print("Oops! That was not a valid number. Try again...")
                emptyLines(1)
        newvalues = {"$set": {"kcal": kcal}}
        mycol.update_one(myquery, newvalues)
        emptyLines(1)
        print("Succefully updated ", name, newvalues["$set"])
    else:
        emptyLines(1)
        print(name + " not found.")
    emptyLines()


def updateName():
    name = input("Product Name: ")
    myquery = {"name": name}
    if mycol.find_one(myquery):
        newName = userChoice = input("New Name: ")
        newvalues = {"$set": {"name": newName}}
        mycol.update_one(myquery, newvalues)
        emptyLines(1)
        print("Succefully updated ", name, newvalues["$set"])
    else:
        emptyLines(1)
        print(name + " not found.")
    emptyLines()


def findOne():
    name = input("Search product: ")
    food = {"name": name}
    x = mycol.find_one(food)
    if x == None:
        emptyLines(1)
        print(name + " not found")
    else:
        emptyLines(1)
        print(x)
    emptyLines()

# Non MongoDB


def emptyLines(x=2):
    print('\n' * x)


def printMenu():
    emptyLines()
    print("-" * 22 + "Menu" + "-" * 22)
    print("1. Show all                 5. Update kcal")
    print("2. Add new product          6. Sort by name")
    print("3. Find product             7. Sort by kcal")
    print("4. Update name              8. Delete product")
    print("0. Exit")
    print("-" * 48)
    emptyLines()


# Main Loop

def main():
    userChoice = None
    while True:
        if userChoice in [1, 2, 3, 4, 5, 6, 7, 8, 99]:
            input("Press Enter to continue")

        printMenu()

    # New while loop, else it would run previous option with valueError
        while True:
            try:
                userChoice = int(input("Please make a choice: "))
                emptyLines(1)
                break
            except ValueError:
                print("Oops! That was not a valid number. Try again...")
                emptyLines(1)

        if userChoice == 0:
            emptyLines(1)
            print("Goodbye")
            emptyLines(1)
            break

        elif userChoice == 1:
            showAll()
        elif userChoice == 2:
            insertOne()
        elif userChoice == 3:
            findOne()
        elif userChoice == 4:
            updateName()
        elif userChoice == 5:
            updateKcal()
        elif userChoice == 6:
            sortByName()
        elif userChoice == 7:
            sortByKcal()
        elif userChoice == 8:
            deleteOne()
    # test option
        elif userChoice == 99:
            showCollections()
        else:
            print("Please choose a correct number (0-8)")


if __name__ == "__main__":
    main()
