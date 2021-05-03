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
my_order = {
    'Wings':0,
    'Cookies':0,
    'Spring Rolls':0,
    'Salmon':0,
    'Steak':0,
    'Meat Tornado':0,
    'A Literal Garden':0,
    'Ice Cream':0,
    'Cake':0,
    'Pie':0,
    'Coffee':0,
    'Tea':0,
    'Unicorn Tears':0,
}
while quit != False:
    order = input(">")
    if order == 'quit':
        quit = False
    else:
        for food_dir in menu:
            for food in food_dir['foods']:
                if order.upper() == food.upper():
                    order = food
                    my_order[food] += 1
                    counter = my_order[food]
                    if food not in order_list:
                        order_list.append(food)
                    exists = True
                    break
            if exists == True:
                print('')
                order_str = (f"** {counter} order of {order} have been added to your meal **")
                print(order_str)
                exists = False
                break
        print('')
print('you have ordered:')
for ordered in order_list:
    counter = my_order[ordered]
    order_str = (f"** {ordered} order of {counter} have been added to your meal **")
    print(order_str)
    print("")
