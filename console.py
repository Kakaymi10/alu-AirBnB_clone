#!/usr/bin/python3
#importing cmd module
import cmd

#creating class HBNBCommand class
class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    #Quitting meth
    def do_quit(self, arg):
        #return quit
        print("Exitting...")
        return True
    
    #help quit
    def help_quit(self):
        #Return quit
        print("Quit command to exit the program")
    
    #Emptyline pass
    def emptyline(self):
        pass
    
    #Exit EOF
    def do_EOF(self, arg):
        """EOF signal to exit the program."""
        print("Exitting")
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
