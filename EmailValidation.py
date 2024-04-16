'''[]	A set of characters	"[a-m]"	
\	Signals a special sequence (can also be used to escape special characters)	"\d"	
.	Any character (except newline character)	"he..o"	
^	Starts with	"^hello"	
$	Ends with	"planet$"	
*	Zero or more occurrences	"he.*o"	
+	One or more occurrences	"he.+o"	
?	Zero or one occurrences	"he.?o"	
{}	Exactly the specified number of occurrences	"he.{2}o"	
|	Either or	"falls|stays"	
()	Capture and group
\w any word character(alphanumeric character)'''
import re
email=input("Enter your email address:\n")
if re.search(r"^[a-zA-Z0-9_ \.]+@([a-zA-Z0-9_]+\.)?\[a-zA-Z0-9_]+\.(edu|com|net|gov|org)$",email,re.IGNORECASE):
    print("valid")
else:
    print("Invalid")    