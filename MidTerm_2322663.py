"""Name of program: MidTerm_2322663.py
   Author of program: Stephanie Roussy
   Last date program was modified: 10/15/21
   Summary of the program's intent:Reads a
   menu text file with item names, wholesale
   and retail prices and how many times an
   item has been ordered in the past month
   to a manager. Reads the same menu
   (however only provides the item name and
   retail price) to the customer. The
   manager will have the ability to update
   the menu with additions and deletions.
   The customers' orders are charged
   appropriate sales tax and are offered
   to provide a tip. Their order summary
   is then printed with subtotals and the
   grand total due. The original menu file
   is updated to reflect the updated count
   of items ordered."""
###############    Manager Program     ##################
def option1 ():
    print("The current menu is read below, including the wholesale prices, retail prices and number of monthly orders placed by customers.")
    # Open file and read menu
    file1 = open('menu.txt', 'r')
    lines = file1.readlines()

    # Create empty lists to store menu items, prices, monthly order count
    menu_item = []
    wholesale_price = []
    retail_price = []
    monthly_orders = []
    for line in lines:
        words = line.split("|")
        words[3]=words[3].replace("\n","")
        menu_item.append(words[0])
        wholesale_price.append(words[2])
        retail_price.append(words[1])
        monthly_orders.append(words[3])
        

    # print column headers
    print("%-20s %-18s %-18s %-18s"%("Item Name", "Wholesale Price", "Retail Price", "Monthly Orders"))
    print("\n")

    # print menu items
    for i in range(len(menu_item)):
       print("%-3s %-20s %-18s %-18s %-18s"%(str(i + 1), menu_item[i], "${:,.2f}".format(float(wholesale_price[i])), "${:,.2f}".format(float(retail_price[i])), str(monthly_orders[i])))

    # loop manager options
    doContinue = 1
    while doContinue == 1:
        print("\n1. Add item")
        print("2. Delete item")
        print("3. Update price")
        print("4. Exit")
        # get manager input
        choice = int(input("Enter choice: "))
        if choice == 1:
            # add item the user inputs along with it's price to existing menu
            item = input("Enter item name: ")
            wPrice = input("Enter item's wholesale price: ")
            rPrice = input("Enter item's retail price: ")
            item += " "
            menu_item.append(item)
            wholesale_price.append(wPrice)
            retail_price.append(rPrice)
            monthly_orders.append(0)
        elif choice == 2:
            # deleted item from menu using item #
            item_no = int(input("Enter item number to be deleted: "))
            wholesale_price.pop(item_no - 1)
            menu_item.pop(item_no - 1)
            retail_price.pop(item_no - 1)
            monthly_orders.pop(item_no - 1)
            for i in range(len(menu_item)):
                print("%-3s %-20s %-18s %-18s %-18s"%(str(i + 1), menu_item[i], "${:,.2f}".format(float(wholesale_price[i])), "${:,.2f}".format(float(retail_price[i])), str(monthly_orders[i])))
        elif choice == 3:
            # update a price of an item 
            item_no = int(input("Enter item number to be updated: "))
            new_price = input("Enter the item's new retail price: ")
            retail_price[item_no - 1] = new_price
            for i in range(len(menu_item)):
               print("%-3s %-20s %-18s %-18s %-18s"%(str(i + 1), menu_item[i], "${:,.2f}".format(float(wholesale_price[i])), "${:,.2f}".format(float(retail_price[i])), str(monthly_orders[i])))
        elif choice == 4:
            # exit manager program (returning them to main menu)
            doContinue = 0
        else:
            print("Invalid choice.")
    file1.close()

    # Write new edited menu in another file called new_menu
    file1 = open('menu.txt', 'w')
    for i in range(len(monthly_orders)):
            theupdates = "%s|%s|%s|%s\n"%(menu_item[i], retail_price[i], wholesale_price[i], monthly_orders[i])
            file1.write(theupdates)
    # close files
    file1.close()

###############    Customer Program    ##################

def option2 ():
    print("The menu is as follows: ")
    # Open files
    file1 = open('menu.txt', 'r')
    file2 = open("bill.txt","w")
    lines = file1.readlines()

    # Create empty lists to store menu items, prices, monthly order count
    menu_item = []
    retail_price = []
    wholesale_price = []
    monthly_orders = []
    total = []
    meal = []
    ordering = 1
    theSum = 0
    monthly_order = []
    azSalesTax = 0.065
   
    for line in lines:
        words = line.split("|")
        words[3]=words[3].replace("\n","")
        menu_item.append(words[0])
        wholesale_price.append(words[2])
        retail_price.append(float(words[1]))
        item_count = int(words[3])
        monthly_orders.append(item_count)
    # print column headers
    print("%-20s %-18s"%("Item Name", "Retail Price"))

    # print menu with numerical index
    for index in range(len(menu_item)):
        print("%-1s %-20s %-20s"%(str(index + 1), menu_item[index], "${:,.2f}".format(float(retail_price[index]))))
    # customer prompt (adding inputs to lists)    
    choice = input("Would you like to place an order? Enter 'Y' for Yes and 'N' for No: ")
    if choice == "N" or choice == "n":
        print("Thank you for visiting Stephanie's")
    elif choice == "Y" or choice == "y":
        food = float(input('Please enter the number corresponding to the item you\'d like to order: '))
        print("You have ordered " + menu_item[int(food) - 1])
        meal = menu_item[int(food) - 1] + "\n"
        theSum += retail_price[int(food) - 1]
        monthly_orders[int(food) - 1] += 1
        # loop customer option to order multiple times
        while ordering == 1:
            place_order2 = input('Would you like to place another order?')
            if place_order2 == "Y" or place_order2 == "y":
                food = float(input('Please enter the item number corresponding to the item you\'d like to order: '))
                print("You have ordered ", menu_item[int(food) -1])
                meal += menu_item[int(food) - 1] + "\n"
                theSum += retail_price[int(food) - 1]
                monthly_orders[int(food) - 1] += 1
            elif place_order2 == "N" or place_order2 == "n":
                ordering = 0
            else:
                print("Invalid Input")

        # order total before tax and tip
        print ("Your total before tax is : $%0.2f" % theSum)

        # calculating their sales tax
        tax = theSum*azSalesTax
        print ("Sales tax : ", str("$%0.2f" % tax))

        # calculating their total
        grandTotal = theSum + tax
        print("Your total with tax is : " + str("$%0.2f" % grandTotal))

        # user prompt to leave a tip
        tipPrompt= int(input("How much would you like to tip : % "))

        # calculating tip
        tip= (tipPrompt/100)*grandTotal
        print("Your tip : ", str("$%0.2f" % tip))

        # grand total with a tip included
        total= tip+grandTotal
        print("Your grand total is : ", str("$%0.2f" % total))

        # printing results in bill.txt
        file2.write("----------------------\n")
        file2.write("You have ordered the following:\n")
        for i in range(len(meal)):
            file2.write(meal[i])
        file2.write("\n")
        file2.write("----------------------\n")
        file2.write("Your total before tax is : $%0.2f" % theSum)
        file2.write("----------------------\n")
        file2.write("Sales tax : $%0.2f" % tax)
        file2.write("----------------------\n")
        file2.write("Your total with tax is : $%0.2f" % grandTotal)
        file2.write("----------------------\n")
        file2.write("Your tip : $%0.2f" % tip)
        file2.write("----------------------\n")
        file2.write("Your Total amount is: $%0.2f" % total)
        # adjusting menu item count in menu.txt
        file1 = open('menu.txt', 'w')
        for i in range(len(monthly_orders)):
            theupdates = "%s|%s|%s|%s\n"%(menu_item[i], retail_price[i], wholesale_price[i], monthly_orders[i])
            file1.write(theupdates)
        
    file1.close()
    file2.close()


############# PROGRAM ################
    
print ("Welcome to Stephanie's:")
option = 1
#Allow user to choose between customer or manager options
while option == 1:
    user = (int(input("Enter 1 for the manager program\nEnter 2 for the customer program\nEnter 3 to exit program ")))
    if user == 1:
        option1()
    elif user == 2:
        option2()
    elif user == 3:
        option = 0
    else:
        print("Invalid choice")
    
       





        



