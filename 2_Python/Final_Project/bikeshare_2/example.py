# imported from stack overflow 
# reference: https://stackoverflow.com/questions/23294658/asking-the-user-for-input-until-they-give-a-valid-response

while True:
    data = input("Please enter a loud message (must be all caps): ")
    if not data.isupper():
        print("Sorry, your response was not loud enough.")
        continue
    else:
        #we're happy with the value given.
        #we're ready to exit the loop.
        break

while True:
    data = input("Pick an answer from A to D:")
    if data.lower() not in ('a', 'b', 'c', 'd'):
        print("Not an appropriate choice.")
    else:
        break



while True:
    try:
        age = int(input("Please enter your age: "))
    except ValueError:
        print("Sorry, I didn't understand that.")
        continue

    if age < 0:
        print("Sorry, your response must not be negative.")
        continue
    else:
        #age was successfully parsed, and we're happy with its value.
        #we're ready to exit the loop.
        break
if age >= 18: 
    print("You are able to vote in the United States!")
else:
    print("You are not able to vote in the United States.")