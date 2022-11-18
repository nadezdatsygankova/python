Question 6
Complete the body of the format_name function. 
This function receives the first_name and last_name parameters and then returns a properly formatted string.

Specifically:

If both the last_name and the first_name parameters are supplied, 
the function should return like so:


def format_name(first_name, last_name):
	# code goes here
	if(first_name and last_name):
		string = "Name: " + last_name + ", "+ first_name
	elif (not first_name and last_name):
		string = "Name: " + last_name 
	elif (first_name and not last_name):
		string = "Name: " + first_name
	else:
	    string =""	
	return string 

print(format_name("Ernest", "Hemingway"))
# Should return the string "Name: Hemingway, Ernest"

print(format_name("", "Madonna"))
# Should return the string "Name: Madonna"

print(format_name("Voltaire", ""))
# Should return the string "Name: Voltaire"

print(format_name("", ""))
# Should return an empty string
