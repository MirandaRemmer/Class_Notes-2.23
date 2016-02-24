contacts = [
	{"last name": "Banana", 
	"first name" : "Diana", 
	"email": "diana@hackbrightacademy.com", 
	"mobile":"(415) 555-5555", 
	"birthday":"February 21"},
	{"last name": "Johnson", 
	"first name" : "Brian", 
	"email": "brian@yahoo.com", 
	"mobile":"(415) 222-2356", 
	"birthday":"June 4"}]

print contacts

contacts[1]["last name"] = "Williams"

print contacts

contacts = {
	"Banana_Diana": 
		{"last name": "Banana", 
		"first name" : "Diana", 
		"email": "diana@hackbrightacademy.com", 
		"mobile":"(415) 555-5555", 
		"birthday":"February 21"},
	"Johnson_Brian":
		{"last name": "Johnson", 
		"first name" : "Brian", 
		"email": "brian@yahoo.com", 
		"mobile":"(415) 222-2356", 
		"birthday":"June 4"}
	}
print contacts
print contacts["Banana_Diana"]["email"]
# for item in contacts:
# 	if contacts[] == "Banana":
# 		contacts["last name"] == "Banananananana"
# 	print contacts

