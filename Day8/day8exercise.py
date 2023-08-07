# While I'm sure there are 100% better ways of doing this as this is really 
# unscaleable but for the sake of getting through the course quickly I went with
# a simple answer.
def prime_checker(number):
    for i in range(2, number):
        if number % i == 0:
            return ("Is prime")
    return ("Is not prime")

print(prime_checker(4))