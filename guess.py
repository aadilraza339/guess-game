number=5
for i in range(5):
	user=input("input any number")
	if number==user:
		print "aap jeet gaye"
		break
	elif user<number:
		print "aapka guess chota hai"
	elif user>number:
		print "aapka guess bada hai"
else:
	print "aap haar gaye"
	