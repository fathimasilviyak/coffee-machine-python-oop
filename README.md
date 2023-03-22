# coffee-machine-python-oop

#### A virtual coffee machine using object oriented programming in python, that takes inputs from user to make the desired type of coffee.

### Tasks of the coffee machine:

1. Prompt user by asking “What would you like? (espresso/latte/cappuccino/):”
   
   a. Check the user’s input to decide what to do next.
   
   b. The prompt will show every time action has completed, e.g. once the drink is dispensed. The prompt will show again to serve the next customer.

2. Turn off the Coffee Machine by entering “off” to the prompt.
   
   a. For maintainers of the coffee machine, they can use “off” as the secret word to turn off the machine. The code will end execution when this happens.

3. Print report.
   
   a. When the user enters “report” to the prompt, a report will be generated that shows the current resource values. 
   e.g. <br />
        Water: 100ml<br />
        Milk: 50ml<br />
        Coffee: 76g<br />
        Money: $2.5

4. Check resources sufficient?
   
   a. When the user chooses a drink, then it will check if there are enough resources to make that drink.
   
   b. E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It will not continue to make the drink but print: “Sorry there is not enough water.”
   
   c. The same will happen if another resource is depleted, e.g. milk or coffee.

5. Process coins.
   
   a. If there are sufficient resources to make the drink selected, then it will prompt the user to insert coins.
   
   b. The user can insert four kinds of coins:
      * Quarters = $0.25
      * Dimes = $0.10
      * Nickles = $0.05
      * Pennies = $0.01
  
   c. It will calculate the monetary value of the coins inserted. E.g. if the inserted coins are: 1 quarter, 2 dimes, 1 nickel, 2pennies, 
     then the monetary value = 0.25 x 1 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52
     
6. Check transaction successful?
  
   a. Check that the user has inserted enough money to purchase the drink they selected. E.g Latte cost $2.50, but they only inserted $0.52 then after counting the coins, it will say “Sorry that's not enough money. Money refunded.”.
  
   b. But if the user has inserted enough money, then the cost of the drink gets added to the machine as the profit and this will be reflected the next time “report” is triggered. E.g. <br />
       Water: 100ml<br />
       Milk: 50ml<br />
       Coffee: 76g<br />
       Money: $2.5
  
   c. If the user has inserted too much money, the machine will offer change. E.g. “Here is $2.45 dollars in change.” The change will be rounded to 2 decimal places.

7. Make Coffee.
  
   a. If the transaction is successful and there are enough resources to make the drink the user selected, then the ingredients to make the drink will be deducted from the coffee machine resources. E.g.<br /> 
    
    Report before purchasing latte:<br /> 
      Water: 300ml<br />
      Milk: 200ml<br />
      Coffee: 100g<br />
      Money: $0<br />
      
      Report after purchasing latte:<br />
      Water: 100ml<br />
      Milk: 50ml<br />
      Coffee: 76g<br />
      Money: $2.5
      
      ###### Resources for each coffee:
      -espresso: water(50ml), coffee(18g), cost($1.5)
      -latte: water(200ml), milk(150ml), coffee(24g), cost($2.5)
      -latte: water(200ml), milk(150ml), coffee(24g), cost($2.5)
  
   b. Once all resources have been deducted, it will tell the user “Here is your latte. Enjoy!”. If latte was their choice of drink.
  
Here the project developed using object oriented programming concepts.
  
### Details of classes used with their attributes and methods:

##### 1. MenuItem Class</span> 
###### Attributes:
- name<br />
(str) The name of the drink. e.g. “latte”

- cost<br />
(float) The price of the drink. e.g 1.5

- ingredients<br />
(dictionary) The ingredients and amounts required to make the drink. e.g. {“water”: 100, “coffee”: 16}

##### 2. Menu Class
###### Methods:
- get_items()<br />
Returns all the names of the available menu items as a concatenated string. e.g. “latte/espresso/cappuccino”

- find_drink(order_name)<br />
Parameter order_name: (str) The name of the drinks order.<br />
Searches the menu for a particular drink by name. Returns a MenuItem object if it exists, otherwise returns None.

##### 3. CoffeeMaker Class
###### Methods:
- report()<br />
Prints a report of all resources. e.g.<br />
Water: 300ml<br />
Milk: 200ml<br />
Coffee: 100g

- is_resource_sufficient(drink)<br />
Parameter drink: (MenuItem) The MenuItem object to make.<br />
Returns True when the drink order can be made, False if ingredients are insufficient. e.g. True

- make_coffee(order)<br />
Parameter order: (MenuItem) The MenuItem object to make.<br />
Deducts the required ingredients from the resources.

##### 4. MoneyMachine Class
###### Methods:
- report()<br />
Prints the current profit. e.g. Money: $0

- make_payment(cost)<br />
Parameter cost: (float) The cost of the drink.<br />
Returns True when payment is accepted, or False if insufficient. e.g. False
  
  
  
  
  
