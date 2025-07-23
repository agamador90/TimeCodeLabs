KINGCAKESLICE = 4.95
CROISSANT = 3.95
CATFISH = 14.95
ROASTBEEF = 13.95
SAUSAGE = 12.95
GUMBO = 5.95
CRAWFISHPIESLICE = 3.65

print("Boudreaux & Thibodeaux's Restaurant ")
print("------------------------------------")
print(f"1. Croissant: ${CROISSANT}")
print(f"2. King Cake Slice: ${KINGCAKESLICE}")
print(f"3. Crawfish Pie (By the Slice): ${CRAWFISHPIESLICE}")
print(f"4. Catfish Poboy: ${CATFISH}")
print(f"5. Roast Beef Poboy: ${ROASTBEEF}")
print(f"6. Sausage Poboy: ${SAUSAGE}")
print(f"7. Gumbo: ${GUMBO}")
print("------------------------------------")
item = int()
amount = int()
list_total = []

def calculationMenu(item,amount): #if the user enter and iten number out of range the function send a void error exception and ask again for enter a new item number
    if item == 1:
        total = CROISSANT*amount
        return total
    if item == 2:
        total = KINGCAKESLICE*amount
        return total    
    if item == 3:
        total = CRAWFISHPIESLICE*amount
        return total      
    if item == 4:
        total = CATFISH*amount
        return total  
    if item == 5:
        total = ROASTBEEF*amount
        return total 
    if item == 6:
        total = SAUSAGE*amount
        return total 
    if item == 7:
        total = GUMBO*amount
        return total             
    
def calculationTotal(list_t):
    amount_t= 0
    for i in list_t:
        amount_t += i
    total = amount_t + amount_t*0.0945
    return total
    
 
def findItem(item):
    if item == 1:
        name = "Croissant"
        return CROISSANT, name
    if item == 2:
        name = "King Cake Slice"
        return KINGCAKESLICE, name        
    if item == 3:
        name = "Crawfish Pie (By the Slice)"
        return CRAWFISHPIESLICE, name    
    if item == 4:
        name = "Catfish Poboy"
        return CATFISH, name
    if item == 5:
        name = "Roast Beef Poboy"
        return ROASTBEEF, name
    if item == 6:
        name = "Sausage Poboy"
        return SAUSAGE, name
    if item == 7:
        name = "Gumbo"
        return GUMBO, name            

def itemAdded(item,amount):
    if item == 1:
        name = "Croissant"
        total = CROISSANT*amount
        return print(f"Item added: {amount} x {name} - {total}")
  
    if item == 2:
        name = "King Cake Slice"
        total= KINGCAKESLICE*amount
        return print(f"Item added: {amount} x {name} - {total}")
    if item == 3:
        name = "Crawfish Pie"
        nameBySlice = "Crawfish Pie (By the Slice)"
        if 0 < amount < 8:

            total= CRAWFISHPIESLICE*amount
            return print(f"Item added: {amount} x {nameBySlice} - {total}")
        else:
            count = 1
            total = 0

            if amount >= 8:
             remain = amount-8
             total = CRAWFISHPIESLICE*8
             while remain > 8:
                total += total
                count += 1
                remain -= 8
             slice = CRAWFISHPIESLICE*remain
             if remain is not 0:
                 return print(f"Item added: {count} x {name} - {total}\nItem added: {remain} x {nameBySlice} - {slice}")
             else: 
                 return print(f"Item added: {count} x {name} - {total}")
            else:
                total = CRAWFISHPIESLICE*amount
                return print(f"Item added: {count} x {name} - {total}")
    if item == 4:
        name = "Catfish Poboy"
        total= CATFISH*amount
        return print(f"Item added: {amount} x {name} - {total}")        
    if item == 5:
        name = "Roast Beef Poboy"
        total= ROASTBEEF*amount
        return print(f"Item added: {amount} x {name} - {total}")
    if item == 6:
        name = "Sausage Poboy"
        total= SAUSAGE*amount
        return print(f"Item added: {amount} x {name} - {total}")
    if item == 7:
        name = "Gumbo"
        total= GUMBO*amount
        return print(f"Item added: {amount} x {name} - {total}")

stop = "False"   

while stop != "True":        
 try:
   menuItem = input("What would you like to order? Type the appropriate number of the menu item or DONE when order is complete:")
   if menuItem != "DONE":
       itemAmount = int(input("How many of that item would you like to order? "))
       menuItem = int(menuItem)
      # print(f"You have ordered {itemAmount} {findItem(menuItem)[1]} for ${findItem(menuItem)[0]} each") 
       print(itemAdded(menuItem,itemAmount))
       list_total.append(float(calculationMenu(menuItem,itemAmount))) 
   else:
        stop = "True"           
 except:
    print("I'm sorry, that is not an appropriate response.Type the appropriate number of the menu item!")
    menuItem = input("What would you like to order? Type the appropriate number of the menu item or DONE when order is complete:")
    if menuItem != "DONE":    
      itemAmount = int(input("How many of that item would you like to order? "))  
      menuItem = int(menuItem)      
      #print(f"You have ordered {itemAmount} {findItem(menuItem)[1]} for ${findItem(menuItem)[0]} each")  
      print(itemAdded(menuItem,itemAmount))
      list_total.append(float(calculationMenu(menuItem,itemAmount)))   
    else:
        stop = "True"   
print("-----------------------")   
print(f"Your Total is: {calculationTotal(list_total):.2f}") 
        