class Team:

    def Team_one(self):
        print("Team one members")

    def Team_two(self):
        print("Team two members")

    def Team_three(self):
        print("Team three members")

    def Team_four(self):
        print("Team four members")

class python_advanced_class(Team):

    def show(self):
        print("python advanced class")
    
obj = python_advanced_class()
obj.Team_four()