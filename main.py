#Write your code below this line ๐
def prime_checker(number):
  if number == 1:
    print("It's nither prime nor composite number.")
    return
  for i in range(2,number//2 + 1):
    if number % i == 0:
      print('It\'s not a prime number.')
      return
      break
  
  print("It's a prime number.")




#Write your code above this line ๐
    
#Do NOT change any of the code below๐
n = int(input("Check this number: "))
prime_checker(number=n)



