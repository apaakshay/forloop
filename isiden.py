isalum="akshay12"
print(isalum.isalnum())
isalum="akshay akjasdhja"
print(isalum.isalnum())
isalpha="akshay"
print(isalpha.isalpha())
isalum="akshay12"
print(isalpha.isalpha())
isdigit="12"
print(isdigit.isdigit())
isdigit="akshay"
print(isdigit.isdigit())


var="akshay"
print(var.isidentifier())
var="akshay12"
print(var.isidentifier())
var="akshay@124"
print(var.isidentifier())
var="44akshay"
print(var.isidentifier())
var="akshay akshay"
print(var.isspace())
var="        "
print(var.isspace())

var="Luminar Techno Lab"
print(var.istitle())
var="Luminar techno Lab"
print(var.istitle())


upper="AKSHAY AP"
print(upper.isupper())
lower="akshay ap"
print(lower.islower())