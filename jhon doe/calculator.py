valid_operators = "1234567890*/+-."

def validateExpression(expression):
    # checking invalid characters like # , % , @ etc
    for char in expression:
        if (char not in valid_operators):
            return False 
        
    # checking if two arithmetic operator are side by side ++ , -- , .. etc
    if(("++" in expression) or ("--" in expression) or ("**" in expression) or ("//" in expression or (".." in expression))):
        return False 
    
    # checking ending   423- , 432+ , -432 , /423.423
    if(expression.startswith("*") or expression.startswith("/") or expression.endswith("+") or expression.endswith("-") or expression.endswith("*") or expression.endswith("/")):
        return False
    
    return expression


expression = input("Enter your expression : ").replace(" ","")

validExpression = validateExpression(expression)
print(validExpression)

if(not validExpression):
    print("Invalid expression")
else:
    output = eval(validExpression)
    print(output)


