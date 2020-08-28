import codecademylib
import pandas as pd

visits = pd.read_csv('visits.csv',
                     parse_dates=[1])
cart = pd.read_csv('cart.csv',
                   parse_dates=[1])
checkout = pd.read_csv('checkout.csv',
                       parse_dates=[1])
purchase = pd.read_csv('purchase.csv',
                       parse_dates=[1])

#Inspect the DataFrames using print and head:

print(visits.head(),cart.head(),checkout.head(),purchase.head())
#Combine visits and cart using a left merge.
visits_cart = visits.merge(cart,how = 'left')

#How long is your merged DataFrame?
#print(len(visits_cart))
#2000 rows

#How many of the timestamps are null for the column cart_time?

null_count = visits_cart.cart_time.isnull().reset_index()

print(len(null_count[null_count.cart_time == True]))

#1652 null rows, it means that many people who visited the site did not put anything in the cart.

#What percent of users who visited Cool T-Shirts Inc. ended up not placing a t-shirt in their cart?
percent_not_carted = float(1652)/float(2000)
print(percent_not_carted)
#82.6 %



#Repeat the left merge for cart and checkout and count null values. What percentage of users put items in their cart, but did not proceed to checkout?
cart_checkout = cart.merge(checkout,how= 'left')
print(len(cart_checkout))
#482 rows , aka 482 people proceeded to cart
null_count = cart_checkout.checkout_time.isnull().reset_index()



print(len(null_count[null_count.checkout_time == True]))
#122  did not check out checked out
pct_not_checked_out = float(122)/float(482)
print(pct_not_checked_out)

#25% of users placed an item in their cart but didnt checkout

#merge all four datasets
all_data = visits.merge(cart,how = 'left').merge(checkout,how = 'left').merge(purchase,how = 'left')

print(all_data.head())

#What percentage of users proceeded to checkout, but did not purchase a t-shirt?



null_count = all_data.purchase_time.isnull().reset_index()
#this will give us the amount of people who went to checkout but didnt purchase the item
not_purchased = len(null_count[null_count.purchase_time == True])

pct_not_purchased = float(len(all_data) - not_purchased) / float(len(all_data))

print(pct_not_purchased)
#21% who checkout do not purchase the item


#Which step of the funnel is weakest (i.e., has the highest percentage of users not completing it)?

#The step that is the weakness is step 1, visiting the site to cart as it has a loss percentage of 83%

#How might Cool T-Shirts Inc. change their website to fix this problem?

#Make the cart more accesible, make the products more appealing, make the add the cart button more attracting.

# calculate average time to purchase
all_data['time_to_purchase'] = \
    all_data.purchase_time - \
    all_data.visit_time




print(all_data.time_to_purchase)


print(all_data.time_to_purchase.mean())
