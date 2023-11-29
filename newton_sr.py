def newton_sqrt():
    x = float(input("Enter the number to find the square root of: "))
    n = int(input("Enter the number of times to improve the guess: "))
    guess = x / 2
    for _ in range(n):
        guess = (guess + x / guess) / 2
    print("The square root of", x, "is approximately", guess)

# Call the function
newton_sqrt()
