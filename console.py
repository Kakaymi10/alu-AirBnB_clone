#!/usr/bin/python3
# Importing cmd module
import cmd


# Creating class HBNBCommand class
class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    # Quitting method
    def do_quit(self, arg):
        """Quit command to exit the program."""
        print("Exiting...")
        return True
    
    def help_quit(self):
        """Display help message for quit command."""
        print("Quit command to exit the program")

    def emptyline(self):
        """Do nothing when an empty line is entered."""
        pass

    def do_EOF(self, arg):
        """EOF signal to exit the program."""
        print("Exiting")
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
