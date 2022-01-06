#import
import random
import time

#Start
dash = "-------------------"
hp = "■"
print("Hello! Welcome to EL PRIMO battle ring!")
while 1:
 name = input("Please enter your username: ")
 if name == "El Primo" or name == "EL PRIMO" or name == "el primo":
  print("Invalid name. Please try again")
 else:
   break
print("Welcome!", name ,"please get ready to fight with El Primo")
time.sleep(1)
print(dash)
print("El Primo: Showtime~")
time.sleep(2)
print(dash)
print("Battle begins in 3 seconds,please get ready")
print(dash)
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
print(dash)
print("Battle Starts!!!")
time.sleep(1)
print(dash)

#data
elhp = 30
php = 30
_def_ = 0
_eldef_ = 0
maxAtk = 7
maxHeal = 7
minAtk = 1
minHeal = 1
elminAtk = 1
elminHeal = 1
elmaxAtk = 7
elmaxHeal = 7
bannedchoice = 0
atklvl = 0
heallvl = 0
maxhp = 30
elatklvl = 0
elheallvl = 0
elmaxhp = 30
#Battle
while 1:
  print("El Primo")
  print("HP:",elhp*hp)
  print(dash)
  time.sleep(1)
  print(name)
  print("HP:",php*hp)
  print(dash)
  time.sleep(1)
  if elhp < 1:
    print("El Primo Loose")
    print("You Win")
    print(dash)
    break
  if php < 1:
    print("El Primo Win")
    print("You Loose")
    print(dash)
    break
  atk = random.randint(minAtk,maxAtk)
  heal = random.randint(minHeal,maxHeal)
  print("What do you want to do?")
  choice = int(input("[1] Attack [2] Heal [3] Defense [4] Buff [5] Nothing: "))
  print(dash)
  #Atk
  if choice == 1:
    ratk = atk-_eldef_
    if ratk < 1:
     ratk = 1
    elhp -= ratk
    print("You choose attack, dealt",ratk,"damage.")
    print(dash)
    choice = 0
     
  #Heal
  elif choice == 2 and php<30:
    print("You choose heal, healed",heal,"HP.")
    php+=heal
    print(dash)
    
  #ErrorHeal
  elif choice == 2 and php >= maxhp:
     print("You are already at full HP,you can't heal, never heal when full hp next time!")
     print(dash)
     
  #ErrorDef
  elif choice == 3:
    _def_+=1
    if _def_ == 4:
       _def_-=1
       print("You choose defense, but your defense is already at max level.")
       
    else:
       print("You choose defense, you have a Level",_def_,"shield now.")
       print(dash)
  #Buff
  elif choice == 4:
    print("What do you want to buff?")
    oice = int(input("[1] Attack [2] Heal [3] Max HP: "))
    if oice == 1:
      minAtk += 1
      maxAtk += 1
      atklvl += 1
      print("You choose buff attack, buffed to Level",atklvl)
    elif oice == 2:
      minHeal += 1
      maxHeal += 1
      heallvl += 1
      print("You choose buff heal, buffed to Level",heallvl)
    elif oice == 3:
      maxhp += 3
      php += 1
      print("You choose buff max HP, your max hp is now",maxhp)
  #Nothing
  elif choice == 5:
     print("You choose nothing, so you do nothing")
     print(dash)
  else:
     print('This is not a selection, game over')
     print(dash)
     print("El Primo Win")
     print("You Loose")
     print(dash)
  if choice != 4:
    bannedchoice = choice
  time.sleep(1)
  if elhp < 1:
    print("El Primo Loose")
    print("You Win")
    print(dash)
    break
  if php < 1:
    print("El Primo Win")
    print("You Loose")
    print(dash)
    break
  elatk = random.randint(elminAtk,elmaxAtk)
  elheal = random.randint(elminHeal,elmaxHeal)
  #Def
  if elhp > 25 and _eldef_ < 3:
    _eldef_+=1
    print("El Primo choose defense, El Primo have a Level",_eldef_,"shield now.")
    print(dash)
  #Buff
  elif elhp > 25 and _eldef_ >= 3:
    ch = random.randint(1,5)
    if ch == 1 or ch == 4:
      elmaxAtk += 1
      elminAtk += 1
      elatklvl += 1
      print("El Primo choose buff attack, buffed to Level",elatklvl)
      print(dash)
    if ch == 2 or ch == 5:
      elmaxHeal += 1
      elminHeal += 1
      elheallvl += 1
      print("El Primo choose buff heal, buffed to Level",elheallvl)
      print(dash)
    if ch == 3:
      elmaxhp += 3
      elhp += 1
      print("El Primo choose buff max HP, El Primo's max hp is now",elmaxhp)

  #Atk
  elif php < 10:
    elratk = elatk-_def_
    if elratk < 1:
      elratk = 1
    php -= elratk
    print("El Primo choose attack, dealt",elratk,"damage.")
    print(dash)
  #Atk_2
  elif elhp > elmaxhp/2:
    elratk = elatk - _def_
    if elratk < 1:
      elratk = 1
    php-=elratk
    print("El Primo choose attack, dealt",elratk,"damage.")
    print(dash)
  #Heal
  else:
    print("El Primo choose heal, healed",elheal,"HP.")
    elhp+=elheal
    print(dash)
  time.sleep(1)
