#activity 2


from contact import Contact

contact_miranda = Contact("Miranda", "Remmer")
contact_virginia = Contact("Virginia", "Slutu")
contact_brad = Contact("Brad", "Pitt")

contact_miranda.mobile = "415 555 5555"
contact_virginia.email = "vs@gmail.com"
contact_miranda.email = "mr@yahoo.com"
contact_brad.email = "brad@gmail.com"
contact_brad.birthday = "July 26"
contact_miranda.notes = "hello word!!!"

#contact list
contact_list = []
contact_list.append(contact_virginia)
contact_list.append(contact_miranda)
contact_list.append(contact_brad)

message = "Hello, World"
for person in contact_list:
	person.send_email(message)
	print "\n"


print "\n"

for person in contact_list:
	if (person.notes != ""):
		print "%s %s's Notes: \n\t %s" % (person.first_name, person.last_name, person.notes)
	else: None

print "\n"

for person in contact_list:
	if (person.notes != ""):
		print "%s %s's Notes: \n\t %s" % (person.first_name, person.last_name, person.notes)
		print "\n"
	else: 
		print "%s %s's contact has no notes" % (person.first_name, person.last_name)
		print "\n"