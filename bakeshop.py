MUFFIN = 5.95
KINGCAKE = 4.95
CROISSANT = 3.95
SCONE = 3.75

print("Boudreaux & Thibodeaux's Bakery ")
print("------------------------------------")
print(f"1. Muffin: ${MUFFIN}")
print(f"2. Muffin: ${KINGCAKE}")
print(f"3. Muffin: ${CROISSANT}")
print(f"4. Muffin: ${SCONE}")
print("------------------------------------")
item = int()
amount = int()
list_total = []

def calculationMenu(item,amount): #if the user enter and iten number out of range the function send a void error exception and ask again for enter a new item number
    if item == 1:
        total = MUFFIN*amount
        return total
    if item == 2:
        total = KINGCAKE*amount
        return total    
    if item == 3:
        total = CROISSANT*amount
        return total      
    if item == 4:
        total = SCONE*amount
        return total  
    
def calculationTotal(list_t):
    amount_t= 0
    for i in list_t:
        amount_t += i
    total = amount_t + amount_t*0.0945
    return total
    
 
def findItem(item):
    if item == 1:
        name = "Muffins"
        return MUFFIN, name
    if item == 2:
        name = "KingCake"
        return KINGCAKE, name        
    if item == 3:
        name = "Croissant"
        return CROISSANT, name       
    if item == 4:
        name = "Scone"
        return SCONE, name
    
stop = "False"   
while stop != "True":        
 try:
   menuItem = input("What would you like to order? Type the appropriate number of the menu item or DONE when order is complete:")
   if menuItem != "DONE":
       itemAmount = int(input("How many of that item would you like to order? "))
       menuItem = int(menuItem)
       print(f"You have ordered {itemAmount} {findItem(menuItem)[1]} for ${findItem(menuItem)[0]} each") 
       list_total.append(float(calculationMenu(menuItem,itemAmount))) 
   else:
        stop = "True"           
 except:
    print("I'm sorry, that is not an appropriate response.Type the appropriate number of the menu item!")
    menuItem = input("What would you like to order? Type the appropriate number of the menu item or DONE when order is complete:")
    if menuItem != "DONE":    
      itemAmount = int(input("How many of that item would you like to order? "))  
      menuItem = int(menuItem)      
      print(f"You have ordered {itemAmount} {findItem(menuItem)[1]} for ${findItem(menuItem)[0]} each")  
      list_total.append(float(calculationMenu(menuItem,itemAmount)))   
    else:
        stop = "True"   
print(list_total)   
print("-----------------------")   
print(f"Your Total is: {calculationTotal(list_total):.2f}") 
        