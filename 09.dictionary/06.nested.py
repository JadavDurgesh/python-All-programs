
stocks = {} 

menu = """

              menu
     

    press 1 for product manger 
    press 2 for customer


"""

m_stasus = True

while m_stasus:
    print(menu)
    choice = int(input("enter the your choice..."))
    if choice == 1:
        satatus = True
        while satatus:
            print(stocks)
            print("product manager")
            specification =  {} #nested dictinary
            brand    = input("enter the brand : ")
            category = input("enter the category...")
            qty      = int(input("enter the qty..."))
            price    = int(input("enter the price.."))

            if brand in stocks.keys():
                if  category == stocks[brand]['category']:
                    qty += stocks[brand]['qty']
                    specification['category'] = category
                    specification['qty'] = qty
                    specification['price'] = price
                    stocks[brand] = specification

            else:

                 specification['category'] = category
                 specification['qty'] = qty
                 specification['price'] = price
                 stocks[brand] = specification

                 print(stocks)


                 choice = input("do you continue......y..")
                 if choice == 'n':
                    satatus = False

                 elif choice == 2:
                    print("customor")

                 for k in stocks.keys():
                    print(f"--------{k}--------")
                    print(stocks[k]["category"],"price : ",stocks[k]['price'])

                    print("customor...")
                    brand_name = input("enter the brand : ")
                    product_name = input("enter the category : ")
                    qty    =       int(input("enter the qty : "))
                    
                    product_price = stocks[k]['price']
                    print("price : ",product_price)
                    total_price = product_price*qty

                    print("total price =",total_price)
                    
                    stocks[k]["qty"] = stocks[k]['qty']-qty

                 my_main_choice = input("do you want to continue  ")
                 if my_main_choice == "n":
                    m_stasus = False
