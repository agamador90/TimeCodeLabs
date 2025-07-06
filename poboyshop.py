CATFISH = 14.95
ROASTBEEF = 13.95
SAUSAGE = 12.95
GUMBO = 4.95

print("Boudreaux & Thibodeaux's Po-Boy Shop")
print("-------------------------------------")
print(f"1. Catfish Poboy: ${CATFISH}")
print(f"2. Roast Beef Poboy: ${ROASTBEEF}")
print(f"3. Sausage Poboy: ${SAUSAGE}")
print(f"4. Gumbo Poboy: ${GUMBO}")
item = int(input("What would you like to order? Type the appropiate number of the menu item:"))

total = 0
while item <1 or item >4:
    item = int(input("Please. Type the appropiate number of the menu item between 1-4:"))
    
if item == 1:
  total = CATFISH + CATFISH*0.0945
elif item == 2:
    total = ROASTBEEF + ROASTBEEF*0.0945
elif item == 3:
    total = SAUSAGE + SAUSAGE*0.0945
elif item == 4:
    total = GUMBO + GUMBO*0.0945  
    
print(f"Your total is: ${total:.2f}")  