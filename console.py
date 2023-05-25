#!/usr/bin/python3
#importing cmd module
import cmd

#creating class HBNBCommand class
class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    #Quitting meth
    def do_quit(self, arg):
        print("Exitting...")
        return True
    
    def help_quit(self):
        print("Quit command to exit the program")

    def emptyline(self):
        pass

    def do_EOF(self, arg):
        """EOF signal to exit the program."""
        print("Exitting")
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
