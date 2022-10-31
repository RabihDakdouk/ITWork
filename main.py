class Shark:
    def __init__(self, name): # this method passes name as a parameter and sets self name = name
        self.name = name

    def swim(self):
        print(self.name + " is swimming.") #creates a method that tells the user that prints the name of the shark and says that its swimming

    def be_awesome(self):
        print(self.name + " is being awesome.") #creates a method that tells the user that prints the name of the shark and says that its being awesome

def main():
    sammy = Shark("Sammy") # creates a method that says the sharks name is Sammy
    sammy.be_awesome() # method that prints Sammy is awesome
    stevie = Shark("Stevie") # creates a method that says the sharks name is Stevie
    stevie.swim() #method that prints Stevie is swimming
    rabih = Shark("Rabih")# creates a method that says the sharks name is Rabih
    
    
if __name__ == "__main__":# if statment that tells the program that if shark is being called
  main()
