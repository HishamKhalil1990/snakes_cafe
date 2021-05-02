menu = [
    {
        'type':'Appetizers',
        'foods':[
            'Wings','Cookies','Spring Rolls',
        ]
    },
    {
        'type':'Entrees',
        'foods':[
            'Salmon','Steak','Meat Tornado','A Literal Garden',
        ]
    },
    {
        'type':'Desserts',
        'foods':[
            'Ice Cream','Cake','Pie',
        ]
    },
    {
        'type':'Drinks',
        'foods':[
            'Coffee','Tea','Unicorn Tears',
        ]
    },
]
welocome_str = """**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************

Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears

***********************************
** What would you like to order? **
***********************************"""
print(welocome_str)
order_list = []
quit = True
exists = False
counter = 1
while quit != False:
    order = input(">")
    if order == 'quit':
        quit = False
    else:
        for food_dir in menu:
            for food in food_dir['foods']:
                if order.upper() == food.upper():
                    order = food
                    exists = True
                    break
            if exists == True:
                print('')
                order_str = (f"** {counter} order of {order} have been added to your meal **")
                print(order_str)
                counter += 1
                order_list.append(order_str)
                exists = False
                break
        print('')
print('you have ordered:')
for ordered in order_list:
    print(ordered)
    print("")