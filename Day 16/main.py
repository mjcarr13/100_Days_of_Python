# from turtle import Turtle, Screen
# timmy = Turtle()
# timmy.shape ("turtle")
# timmy.color ("DarkOrange2")
# timmy.forward(100)
#
# #Deosn't seem like there's a need to print here, and the objects go best iun one part fo the code together
#
#
# my_screen = Screen()
# my_screen.exitonclick()

#from prettytable we import a Class called PrettyTable
from prettytable import PrettyTable
table = PrettyTable()
#we can add columns thusly - adding a field name (header) and then the data underneath

table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
#fucntionally the below operates like a dictionary. If you printed it was was, you'd get:
#{'base_align_value': 'c', 'Pokemon Name': 'c', 'Type': 'c'}
#which means to change the attribute globally you can just go
table.align = "l"
print(table.align)
print(table)