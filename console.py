#!/usr/bin/python3
"""This module implements a cmd console for HBNB."""

import cmd


class HBNBCommand(cmd.Cmd):
    """HBNB command-line interface."""

    prompt = "(hbnb) "

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
