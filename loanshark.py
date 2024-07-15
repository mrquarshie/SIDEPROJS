print ("Loan Shark")
clientname =input ("Your name is: ")
clientbank = input("Bank: ")
clientage = input ("How old are you? ")
if int(clientage) < (18):
    print("You are not eligible to apply for the loan")

elif int(clientage) >= (18):
    print("Qualified, Let's Continue...")
clientms = input ("Whats your Marrital status?")
if clientms== "Single":
    print("Unfortunately you are not eligble to take loan from loanShark")
elif clientms=="Married":
    print("Successful, let's continue...")

print("To prove you are human, you need to type a word  of  5 letters or more")

proof = input("type here")
if len (proof)< 5:
    print("You're not Human")   

elif len(proof)>= 5:
    print("Proven you are Human, let's continue...")   

print("This is your provided account number")
print("0106188020192827")