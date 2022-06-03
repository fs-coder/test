food = input("Are you starving?")
if food == 'yes'.lower():
	food_type = input("what would you like to fill in your tummy? bitterly healthy or deliciously unhealthy?")
	if food_type == 'bitterly healthy'.lower():
		print("Being healthy is Important")
	else:
		print("Your tummy will gonna cry!")
else:
	print("You must eat something")