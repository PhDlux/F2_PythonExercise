
problem = int(input("Enter a number to a solve a specific number (1-5). Press 0 to exit: "))
match problem:
    case 1:
        # 1
        def celsiustofahrenheit():
            temperature = float(input("Enter temperature as celsius: "))
            fahrenheit = temperature * (9/5) + 32
            return f"{fahrenheit:.2f}"

        print("Fahrenheit: ", celsiusToFahrenheit())
    case 2:
        # 2
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        num3 = int(input("Enter third number: "))

        if num1 > num2 and num1 > num3:
            print("Maximum: ", num1)
        elif num2 > num1 and num2 > num3:
            print("Maximum: ", num2)
        else:
            print("Maximum: ", num3)
    case 3:
        number = int(input("Please enter a number: "))
        temp = number
        largest = 0
        smallest = 10
        count = 0
        while temp != 0:
            rem = temp % 10
            if rem > largest:
                largest = rem
            if rem < smallest:
                smallest = rem
            count += 1
            temp //= 10

        print("Number of digits in the given number is: ", count)
        print("Smallest number is: ", smallest)
        print("Highest number is: ", largest)

    case 4:
        number = int(input("Enter a number: "))
        i = 1
        total = 0
        while i <= number:
            total += i
            i += 1
        print("Total: ", total)

    case 5:
        def decToBinary(dec):



