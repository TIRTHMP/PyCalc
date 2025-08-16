a = int(input("Enter number 1:"));
b = int(input("Enter number 2:"));

c = (input("Enter a operation : +, -, *, /, %: "));

if c == '+':
    print ("The sum is", a + b);

elif c == '-':
    print ("The difference is", a - b);

elif c == '*':
    print ("The product is", a * b);

elif c == '/':
    if b != 0:
        print ("The quotient is", a / b);
    else:
        print("Error: Division by zero is not allowed.");

elif c == '%':
    if b != 0:
        print ("The modulus is", a % b);
    else:
        print("Error: Division by zero is not allowed.");


