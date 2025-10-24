
#© 2025 Irina Evdokimova. All rights reserved.


#creates the class for budget categories
class Category:


    #initializes the category name and an empty ledger to hold transactions
    def __init__(self, category_name):
        self.category_name = self._strip_text(category_name)
        self.ledger = []


    #returns a formatted string representation of the category according to the requirements:
    def __str__(self):         
        #declares the line length for the output
        width = 30
        
        #adds a header placing the name of the category in the center of the first line
        star_left = (width - len(self.category_name))//2
        star_right = width - star_left - len(self.category_name)
        output_string = '*'*star_left + self.category_name +  '*'*star_right

        #adds a table of transactions according to the requirements: the table row should be length of 30 symbols, include a left-formatted transaction description, a right-formatted transaction amount, and at least one space between them
        for ledger_item in self.ledger:
            #formats transaction amount as "x.xx" 
            output_amount = self._format_amount(ledger_item["amount"])
            #formats transaction descriptions: if a transaction description is too long for the format, its visible part should be shortened 
            output_description = ledger_item['description'][:(width -1 - len(output_amount))]

            #adds transaction descriptions and transaction amounts to the output string formatted according to the requirements
            output_string += '\n' + output_description + ' '*(width - len(output_description) - len(output_amount)) + output_amount
        #adds the balance formatted as "x.xx"
        output_string += f'\nTotal: {self._format_amount(self.get_balance())}'
        return output_string


    #creates a deposit record for the category
    def deposit(self, amount, description = ''):
        #validates the input amount
        amount = self._validate_input_amount(amount)
        #removes leading and trailing spaces
        description = self._strip_text(description)

        self.ledger.append({'amount': amount, 'description': description})


    #calculates the balance of the category
    def get_balance(self):
        return sum(map(lambda ledger_item: ledger_item['amount'], self.ledger))        


    #calculates total spendings in the category
    def category_expenses(self):
        return sum(record['amount'] for record in self.ledger if (record['amount'] < 0) and (not record['description'].startswith('Transfer to')))    


    #creates a withdrawal record if there are sufficient funds
    def withdraw(self, amount, description = ''):
        #validates the input amount
        amount = self._validate_input_amount(amount)
        #removes leading and trailing spaces
        description = self._strip_text(description)

        if self.check_funds(amount):
            self.ledger.append({'amount': amount*-1, 'description': description})
            return True
        else:
            return False


    #transfers the amount to the destination category if funds are sufficient 
    def transfer(self, amount, destination_category):
        #validates the input amount
        amount = self._validate_input_amount(amount)

        if self.check_funds(amount):
            self.ledger.append({'amount': amount*-1, 'description': f'Transfer to {destination_category.category_name}'})
            destination_category.deposit(amount, f'Transfer from {self.category_name}')
            return True
        else:
            return False


    #checks if there is enough funds left in the category
    def check_funds(self, amount):
        #validates the input amount
        amount = self._validate_input_amount(amount)

        return amount <= self.get_balance()


    #validates the input amount
    def _validate_input_amount(self, amount):
        try:
            return abs(float(amount))
        except (ValueError, TypeError):
            raise ValueError('Invalid amount value.')


    #removes leading and trailing spaces
    def _strip_text(self, text):
        return text.strip()


    #formats the amount according to the requirements for the output
    def _format_amount(self, amount):
        return f'{amount:.2f}'


#creates a string for the output with a bar chart representing the percentage of spendings in the total spendings for selected categories formatted according to the requirements  
def create_spend_chart(categories):
    #calculates the total spendings for all categories
    total_expenses = sum(cat.category_expenses() for cat in categories)

    #creates a dictionary with category_name attributes and rounded (down to 10%) percentage of spendings in the total spendings for the selected categories
    category_and_expenses_percentage = {cat.category_name: 0 if total_expenses == 0 else int((abs(cat.category_expenses() / total_expenses * 100) // 10)*10) for cat in categories}

    #creates the output string and adds the title
    spend_chart = 'Percentage spent by category\n'

    #adds Y-axis with percentages and bars of the chart
    for percentage_axis_value in range(100, -10, -10):
        #adds Y-axis elements
        spend_chart += f" "*(3-len(str(percentage_axis_value))) + f'{percentage_axis_value}|'

        #adds bars to the chart corresponding to each category, order matches the input list   
        spend_chart += ''.join(' o ' if value >= percentage_axis_value else '   ' for value in category_and_expenses_percentage.values()) +' \n'

    #adds X-axis with the selected categories
    spend_chart += '    ' + '-'*(3*(len(category_and_expenses_percentage)) + 1)

    #finds the maximum name length among the names of the selected categories
    max_cat_name_length = max(len(key) for key in category_and_expenses_percentage)

    #writes the selected category names vertically under X-axis
    for key_index in range(0, max_cat_name_length):
        spend_chart += '\n    '
        for key in category_and_expenses_percentage:        
            try:
                spend_chart += ' ' + key[key_index] + ' '
            except (IndexError):
                spend_chart += '   '    
        #adds a space at the end of the line to get all lines of the chart of equal length according to the requirements 
        spend_chart += ' '

    return spend_chart


food = Category('Food')
food.deposit(1000, 'deposit')
food.withdraw(30.15)
food.withdraw(25.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
print(food)

clothing.withdraw(25.15, 'Dress')
clothing.withdraw(15.15, 'Belt')
print(clothing)

auto = Category('Auto')
auto.deposit(200, 'deposit')
auto.withdraw(100, 'insurance')
auto.withdraw(50, 'fuel')
print(auto)

print(create_spend_chart([food, clothing, auto]))    
