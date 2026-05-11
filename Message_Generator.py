

"""  MESSAGE GENERATOR"""


"""This program generates a personalized message based on the user's name, age, and birth month. 
It combines these inputs to create a unique message that reflects the user's characteristics and the season they were born in."""




def month(birth):
    if birth==1:
        print("🌦️ January\nFresh beginnings in the cool breeze—may your year start bright and strong")
    elif birth==2:
        print("🌤️ February\nWarm hearts in the chill air—carry courage and kindness everywhere")
    elif birth==3:
        print("🌸 March\nSpring whispers new hope—let your dreams bloom with the season!")
    elif birth==4:
        print("🌞 April\nSunny skies and gentle rains—balance brings growth and joy!")
    elif birth==5:
        print("🌼 May\nGolden days ahead—shine with energy and positivity!")
    elif birth==6:
        print("☀️ June\nSummer warmth surrounds you—let your courage glow like the sun!")
    elif birth==7:
        print("🌴 July\nBright skies and bold spirits—adventure awaits in every moment!")
    elif birth==8:
        print("🌻 August\nFields of sunshine—stand tall and fearless like the sunflower!")
    elif birth==9:
        print("🍂 September\nCool winds of change—embrace new paths with strength!")
    elif birth==10:
        print("🍁 October\nAutumn colors remind us—courage is as beautiful as transformation!")
    elif birth==11:
        print("❄️ November\nChilly nights, warm hearts—gratitude keeps us strong!")
    elif birth==12:
        print("🎄 December\nWinter lights sparkle—carry joy and courage into the new year!")
    else:
        print("Please input correct month")





def msg(name,age):
    total=len(name)+age

    if total>=50:
        print(f"{name}, You are lucky and courageous")
        

    elif total>=30:
        print(f"{name}, You are kind and brave")
           

    elif total>=20:
        print(f"{name} ,you seems nice person")
    
    elif total<=18:
        print(f"{name} ,You have a lovely heart!")
            

    else:
        print(f"{name} ,You have a gentle and warm heart!")


            

while True:

    name=input("Please enter your name: ")
    age=int(input("Please enter your age: "))
    birth=int(input("Please enter your birth month (1-12): "))

    month(birth)
    msg(name,age)

    cont=input("Do you want to continue? (y/n): ")
    if cont.lower() !="y":
        print("Thank you for using the message generator! Goodbye!")
        break

    
