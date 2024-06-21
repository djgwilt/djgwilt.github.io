# This Python code is inspired from The Friendship Algorithm mentioned in The Big Bang Theory in Season 2, Episode 13.
# It is slightly modified to account for inifinite loops and invalid user inputs.
# Note that the ESC where recreational activities are compared is set to n > 6.
# Created by Matthew Soh, 9M (22/9/2023)

from colorama import Fore

def system(outp):
  print("System Message:",outp)
def cooper(outp):
  print("Cooper:",outp)
def kripke(outp):
  print("Kripke:",outp)
def inpMess():
  return input("Input ('Yes' or 'No'): ")
def invInp(i):
  print("Invalid input.")
  if i == 3:
      print(Fore.RED + "\nSystem Termination.")
      quit()

print(Fore.RED + "Note: The user will have to act as both Sheldon Cooper and Barry Kripke. However, this code imitates the watcher's view of only hearing what Cooper says.")

print()
print(Fore.RESET + "[Placing Phone Call...]")
kripkeAns = None
for i in range(4):
  print()
  system("Is Kripke currently available to be contacted?")
  kripkeAns = inpMess()
  if kripkeAns == "Yes":
    break
  elif kripkeAns == "No":
    cooper(input("As Cooper, please leave a message for Kripke.\nMessage: "))
    print("[Waiting for a certain interval of time...]")
    if i == 3:
      print(Fore.RED + "\nUnfortunately Kripke is unable to be contacted.")
      quit()
  else:
    invInp(i)
    if i == 3:
      quit()

print()
cooper("Would you like to share a meal?")
for i in range(4):
  print()
  system("Does Kripke want to share a meal with Cooper?")
  mealAns = inpMess()
  if mealAns == "Yes":
    print("[Cooper and Kripke share a meal together.]")
    quit()
  elif mealAns == "No":
    break
  else:
    invInp(i)

print()
cooper("Do you enjoy a hot beverage?")
for i in range(4):
  print()
  system("What beverage does Kripke enjoy?")
  bevAns = input("Input ('Tea', 'Coffee', 'Cocoa' is preferred): ")
  if bevAns == "Tea" or bevAns == "Coffee" or bevAns == "Cocoa":
    bevAns.lower()
    print("[Cooper and Kripke share %s together.]" %bevAns)
    quit()
  else:
    break

recs = []
i = 0
n = 0
chooseAct = False
while True:
  print()
  cooper("Recreational activity? Tell me one of your interests!")
  system("What recreational activity does Kripke want to offer?")
  recAns = input("Input (Recreational Activity): ")
  system("Does Cooper like this activity?")
  likeAns = inpMess()
  if likeAns == "Yes":
    break
  elif likeAns == "No":
    system("Oh well...")
    recs.append(recAns)
    if n == 5:
      chooseAct = True
      break
    system("Let's try again!")
    n += 1
  else:
    i += 1
    invInp(i)
  
print()
if chooseAct:
  system("Cooper will have to choose the least objectionable action.")
  for i,c in enumerate(recs):
    print("Option %d: "%(i+1), c)
  system("Which option does Cooper choose?")
  for i in range(4):
    print()
    try: 
      optionAns = int(input("Input (no. from 1 onwards): "))
      cooper(recs[optionAns-1]+'!')
      break
    except:
      invInp(i)
cooper("Why don't we do that together?")


  
