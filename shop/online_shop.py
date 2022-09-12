
product = ['sugar', 'garri', 'flour']
product_qty = {'sugar':50,'garri':45,'flour':47}
product_price = {'sugar':25, 'garri':28, 'flour':30} # All prices in dollars
#cart = {'product': 'unavaliable' , 'price': 0, 'quantity':0}
#final_cart = []

final_cart = []
print('***Welcome To Cyrptex Supermarket***')
print('Avaliable Products: ' + str(product))
shop = str(input('what: '))
while shop == 'opened':
    #print('***Welcome To Cyrptex Supermarket***')
    #print('Avaliable Products: ' + str(product))
    #final_cart = []
    if shop == 'opened':
        name = str(input('Please input name of item you want to purchase in lowercase: '))
        item_name = name.split(',')
        count = 0
        while True:
            for i in item_name:                    
                if i in product :
                    print('Quantity avaliable: '+ str(product_qty.get(i)))
                    quantity = int(input('Please input number of quantity: ' ))
                    if product_qty.get(i) >= quantity:
                        print(i + ' is avaliable in your proposed quantity')   
                        print('$'+ str(product_price.get(i)) + ' per quantity')
                        cart = {'product': 'unavaliable' , 'price': 0, 'quantity':0}
                        #final_cart = []
                        confirm_order = str(input('Confirm order [y/n]: '))
                        
                        if confirm_order == 'y':
                            cart['product'] = i
                            cart['price'] = '$'+ str(product_price.get(i)* quantity)
                            cart['quantity'] = quantity
                            product_qty[i] -= quantity
                            #print(product_qty)
                            cart.update(cart)
                            #final_cart = []
                            final_cart.append(cart)
                            print('Cart: '+ str(cart) )
                            print('Items have been Successfully added cart')
                            item_name.remove(i)
                            print(item_name)
                        elif confirm_order == 'n':
                            print('Item was not added')   
                    elif product_qty.get(i) < quantity:
                        print('Item not avaliable in this quantity')
                elif i not in product:
                    print(i +' not avaliable')
                    continue                   
            if len(item_name) == 0:    
                purchase = str(input('Stil want to make purchase [y/n] : '))
                if product_qty.get(i) >= 0  and purchase == 'y':
                    #final_cart.append(cart)
                    continue
                elif purchase == 'n':
                    #final_cart.append(cart)
                    print('Main Cart: '+  str(final_cart))
                    break              
    elif shop == 'closed':
        break
    else:
        print('Something went wrong')
        continue   
    """purchase = str(input('Stil want to make purchase [y/n] : '))
    while purchase == 'y':
        if product_qty.get(i) >= 0:
            continue
        else:
            break"""
