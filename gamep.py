from time import *
from random import *
print("""%%###%%%%%%%%%%%@@@%%%%@@@%%%%%%@@@@@@@@@@@@@
@@@@%@@@@@@%%%%%@@@@@@@@@@@@@%@@@@@@@%%%%%%%%%%###%%%%%%%%%%%@@@@%%%@@@%%%%%@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%@%%@@@@%%%%%%%%%%##%#########%@@@@@%%%%%%%%%@@@@@@@@@@@@@@@@
@@@@%@@@@@@@@@@@@@@@@@@@@%%%%%%%%%%%@@%%%%%%%#######**##%#%@@@@@@%%#%%%%%@@@@@@@@@@@@@@@@@
@@@@%@@@@@@@@@@@@@@@@@@@%%%%%%%%%%%%%%%%%%%%%####*#######%%@@@@@@%%%%%%%%@@@@@@@@%%%%%%%%@
@@@@@@@@@@@@@@@@@@@@@@@%%%%%%%%%%%%%%%%%%%%#####**#**##%%%@@@@@@@%#+*%%%%%%***####%%%%%%%%
@@@@@%@@@@@@@%%@@@@@@@%%%%%%%%%%%%%%%%%%%%##*******+*#%%%%@@@%@@@%##%##*#####%%%@%%%%%%@%@
@%@@@%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#%##*++*+++*+*#%%%%%%%%@%@@@#%%%%%%%%%%%%%%%%%%%@@%@
@%@@@%%%%%%%%%%%%%%%%%%%%####%%%%%%##%%%%+-=++=++=*%@%%%%%%%@@@@@%##%@@%%%%%%%%%%%%%%%%%%@
%%@@@%%%%%%%%%%%%%%###########%%%%%%#%%#%*--=-=+#%@%%%%%%%%@@@@@%%#%%@@%%@@%%%%%%%%%%%%%%%
##%@@%%%%%%##################*#%##%%#%%#%%=--+#%@%%%%%%%%%@@@@@@%##%%%%%%%%%%%%%%%%%%%%%%%
###@@%%%#######%##################%%#%%#%%*+%%%%%%%%%%%%%%%%@@%#####%%%##%%%%%%%%%%%%%%%%%
##*@@%%%%%%#######**********#%#*##%##%%#%%%@@@@%%@@@@%%%%%%@%###***#%%%%%%%%%%%%%%%%@@@@@@
+*+@@%%%%%%%######***#%%%%%####**%%%%%%%%%@@@@%%@@@@%%%#%@@@%*****+%%%#%%%%%%%%%%%%@@@@@@@
==-#@%%%%%%#%######*#%%%%%%%%%%##%@%%%%%@@@%%%%@%%%%%%%@%@@@#***++%%%%%%%%%%%%%%%%@@@@@@@@
+=-+%%%%%%%%######%%%%%%%%@@%%%%#%%%%%%@@@@@@%%%%%%#%@@@@@@#***+*%%%%%%%%%%%%%@@@@@@@@@@@@
+++=#%#%%%%%@%###*#%%%%%%@@@@@%@@@%%%%##@@@@@@@%%*#@@@@@@%****+#%%%%%%%%%%%%%%%%@@@@@@@@@@
##%%#%%#%%%@@@@%%%%%%%%%%%@@@@%%@%%%#%%#@@@@@@@@@%%@@@@@%##*+*%%%%%%%%%%%%%%%%%%@@@@@@@@@@
@@@@@@@@%%%%%%%%#%@@%%%%%%%%%@@@@@@@%%%#%@%@@@@@@@%%@@@#***+#%%%%%%###%%%%%%%@@@@@@%%%%%%%
%@@@@@@@@@@@@%%%%@@@%%##%%%%%%@@@@@@@%@%%@%%%%@@@@@@@%#****%%%%%%%##%%%%%%%%%%%%%%%%%%####
%@@@@@@@@@@@@%%%%@@%%######%%%%%%%%@@@@@%%@%%%%%@@@@%##*+*%@%%%%%##%%%%%%######%#####***##
%%%@@@@@@%@@@@%%@@@%%#**#%@@@@@%%%%%%%@@%%@@%%%%%%%@@%##%%%%%%@%*****####*******%%###*****
%%%%%@@@%%@@@@%%@@@%#**%@@@@@@@@@@@@%%%%@%%@%%%%%%%%@@@@%%%%%%%*++***************########*
@@@@@%%%*%@@@@@@@@%%*#@@@@%#%%%@@@@@@@@%%@%%%%%%%%%%%@@@@%##%#+++++++++****************#*#
@@@@@@@@@@@@@@@@@%###@@@@%%#+*##%@@@@@@@@@@%#%%%@@%%%@%@@@*+*+++++++++++********###***+*%@
#%%@@@@@@@@@@%@@%##%@@@@%%##*#%%@@@%%@@@@@%%####@@@%%@%%%@+=======++++++++**+****###***@@@
#######%%@@@@@@@##@@@@@@@@%%%%%#%##%@@@@%#%%*####%%%%@#%%%+=============+++++****#####%@@@
***########%@@@@#@@@@@@@%##%##*%%%%@@@@%##%#*######%%%%%%%+===============+++******##%%@@@
***++***#*%%%%@%%%@@@@@@@@%%%##%%%@@@@@%##%**####%%#####%%=--====-========++****###%#%%@@%
%%%###*+=*#%%%%%@@%%%%%%@@@@%%%%%%@@@@@%*##***#########%%#----=============+##*####*%%%%@%
%%%%%%%%%%%%%%%%@@%%%%@%%@@@@@%%%%@@@@@%=+#+**########%@*---------===========***++++#%%%%%
%%%%%%%%%*#@%%@@%%%%%%@@@%%%@@@@@@@@%%*-.++=*####%%%%%%%------------++==++++=++++***#%%%%%
**##%****++*%%%%####%%%%@@%%%@@@%%%#***+-*-=*###@%%%%%@+---------=-===-==++++*#######%%%%%
***+++***++++#%#######%%%%@@%%%%%@%###*+=*+***#%%%%%%@@----=------=++===+===+#%#*##*#%%%%%
**++++++++++++######%%%%%%%%@%%%%%##****+#+***#%%%%%%@#--====-----==+***++*####****###%%%%
**+++***+++++++*###%@@@%%%%%%%%%%#########+**#%%%%%%@%%#======-----=++**+=++**++=+######**
***####*****+++==+*#%@@%%%%%%%%%%%%%%%%%%%#%%%%%%%%%%@@%--======---=++**++*+**++*+++++=-:=
*######++****++++====*@@%%%%%%%%%%%%%%#%%#%%%%%%%%%@@%%%#%%%%%#+==++=+*+++++++===--:..   .
*****++++++**++++=====+@@@@@@@%%%%%%%%%%%%%%%%%%%%####%%%%%%%##*++++++++=====-:.        .-
++++++++++++++*+++++++*%@@@@@@@@@%%%%%%%%%%%#%%%%#####%##########**+++==-::.        ..::-+
+++++++++++++++++++++*@%%@@@@@@@@@%%%%%%%%%%%%%#*%#**#########*****+==-.        .:::-=+===
*****+++++***+++++++++%@%%@@@@@@@@@%%%%%%%%%%%#*#**%%%%%###***+=-:.        ..:-+*++=+++***
####*++++++***++++++*#%%%%%%@@@@@@%%%%%%%##%%%##+#%%%%##*+=-:.    .....:::--=+*#**++***##*
####**+*++++*********%%%%@%%#%%%%@%%%%#####%%###%%##*+-:.    .:---=====--=+*****++*#######
#**##*+**+++*********#%%%%%%%%%#####%#%%%%%%%##*+=-. ...:-==+*******+=++++*******#####%%%%
##*******++**++++******%%%%##%%%%%%%@%%%%####*=-...:-=+******####%##*********##**##%%%%%%#
************#***#******#@%%%%###%%%%#####*=----=+********#######%%%%%#****#####**##%%##***
*********###%#####******%@@@%%%%%%##*+==+++*#####*****########%%%%%%%%%%%%%%###***##****##
**********#%#######*****#%%%%%##+====+*######***##########%%%%%%%%%%%%####%%%##**##*******
******###########***********++++*#####*%%%%##################%%%%%%%%%******###*###*******
**################***++====+*###%%%%##%@@#*#%%%########++%%#####%%%%%########**##%%%######
*###############**+===++***##*#%@%%%%@@@%%%%%%%%#########%%%%%%##%%%%#######%%%%@@@@@@@@@%
***#######***++==+*****##########%%%%%%@%%%%%%%%#*++**######%%%############%@@@@@@@@@@@@@@
##******++==+**#####################%%%%%%%%%%%#*+=+***################***#%@@@@@@@@@@@@@@
**++====++***###%%%%#%%%%%%%%%%%%##%%%*%%%%%%%###****###########%@%#####%%%%%@@@@@@@@@@@@@
===++**#############%%%%%%%%%%%%%%%%%%%%%%%%###################@@@@%#**#%%###%@@@@@@@@@@@@
*#######%%%%#%%%%%%%%%%%%%####%%%%%%%%%%%%%%###%#############%@@@%%%#**#%%%%%%@@@@@@@@@@@@
##%%%%%%%%%%%%%%%%%%%%%%%%@%%%%%%%%%%%%%%%%%%%%%##########%@@@@%%%@%%%##%%%%@@@@@@@@@@@@@@
%%%%%%%%%%%%%%%%%%%@%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#######%%%%%%%#%%%%%%#%%%%%%%%%@@@@@@@@@""")
print("""
      Давние враги Argus и Nolan вновь встретились в битве за право сильнейшего. Argus-бессмертный воин, который обманул саму смерть, решил бросить вызов
      Nolan'у-учёному, который решил отказаться от своих идей и использовать магию, для своего величия.""")

class Person:
    def __init__(self,name):
        self.name=name
        self.health = 100
        self.damage = 20

    def aptechka(self,name):
            self.health += 10
            print(f"{self.name} использовал на себе аптечку и исцелил 10 едениц здоровья. После использоваия апетчки у него стало {self.health}.")

    def attack(self,enemy):
            enemy.health -= 20
            print(f"{self.name} атаковал {enemy.name} нанеся 20 едениц урона и у врага осталось {enemy.health} едениц здоровья.")


unit1 = Person("Argus")
unit2 = Person("Nolan")

while unit1.health > 0 and unit2.health > 0:
    if randint(0,1)==1:
        sleep(2)
        unit1.attack(unit2)
    else:
        sleep(2)
        unit2.attack(unit1)
    
    if randint(0,10)==10:
        unit1.aptechka(unit1)
    if randint(0,10)==9:
        unit2.aptechka(unit2)

if unit1.health==0:
    print("В ожесточённой схватке победил",unit2.name)
if unit2.health==0:
    print("В ожесточённой схватке победил",unit1.name)