##Write program to calculate the discount cost


##User input original cost of item
originalPrice = float(input("Enter the original cost of item: "))

##Determine the discount cost
if originalPrice < 128:
  discountPrice = originalPrice * .08
else:
  discountPrice = originalPrice * .16
  

##Print the discount price
print ("The discount price is: %2f" % discountPrice)

