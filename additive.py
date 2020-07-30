while True:
	print("\nWelcome to the program of additive cipher --------")
	from Crypto.Util.number import *
	print("For encryption enter : 1 and for decryption enter : 2")
	a=int(input("enter the choice : "))
	key = int(input("enter the key : "))
	list1=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	if a==1:
		plain = input("enter the plain text : ")
		for i in plain:
			index=list1.index(i)
			cipher=pow((index+key),1,26)
			cipher=list1[cipher]
			cipher=cipher.upper()
			print (cipher,end='')
	if a==2:
        	plain = input("enter the cipher text in lower case : ")
        	for i in plain:
                	index=list1.index(i)
                	cipher=pow((index-key),1,26)
                	cipher=list1[cipher]
                	print (cipher,end='')

