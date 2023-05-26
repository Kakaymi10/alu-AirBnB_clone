#!/usr/bin/python3
"""
This module defines the console for the AirBnB clone project
"""

import cmd
import re
from shlex import split
from models import storage
from models.base_model import BaseModel

def parse(arg):
    curly_braces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)
    if curly_braces is None:
        if brackets is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lexer = split(arg[:brackets.span()[0]])
            retl = [i.strip(",") for i in lexer]
            retl.append(brackets.group())
            return retl
    else:
        lexer = split(arg[:curly_braces.span()[0]])
        retl = [i.strip(",") for i in lexer]
        retl.append(curly_braces.group())
        return retl

class HBNBCommand(cmd.Cmd):
    """
    This class defines the console for the AirBnB clone project
    """
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """
        Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """
        EOF command to exit the program
        """
        return True

    def emptyline(self):
        """
        Empty line
        """
        pass

    def default(self, arg):
        """This is the default behavior for cmd module when input is invalid"""
        argdict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        match = re.search(r"\.", arg)
        if match is not None:
            argl = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", argl[1])
            if match is not None:
                command = [argl[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in argdict.keys():
                    call = "{} {}".format(argl[0], command[1])
                    return argdict[command[0]](call)
        print("*** Unknown syntax: {}".format(arg))
        return False

        def do_create(self, args):
        """
            Creates a new instance of a class,
            saves it (to the JSON file) and prints the id.
            Usage: create <class_name>
       """
        # If the class name is missing,
        # print ** class name missing ** (ex: $ create)
        if len(args) < 1:
            print("** class name missing **")
            return
        # If the class name doesn’t exist,
        # print ** class doesn't exist ** (ex: $ create MyModel)

        # convert the args to a list
        args = args.split()

        # the 1st element of the list is the class name
        class_name = args[0]
        if class_name not in self.__all_classes:
            print("** class doesn't exist **")
            return
        # print(self.__all_classes)
        # eval() interprets a string as a piece of python code
        new_object = eval(class_name + "()")
        new_object.save()
        print(new_object.id)
        storage.save()

    def do_show(self, arg):
        """Show the string representation of an instance."""
        args = arg.split(" ")
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in models.storage.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            objects = models.storage.all()
            key = "{}.{}".format(args[0], args[1])
            if key in objects:
                print(objects[key])
            else:
                print("** no instance found **")


    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id
        """
        args = shlex.split(arg)
        if not arg:
            print("** class name missing **")
        elif args[0] not in models.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            if key not in models.storage.all():
                print("** no instance found **")
            else:
                del models.storage.all()[key]
                models.storage.save()

    def do_all(self, arg):
        """
        Prints all string representation of all instances
        based or not on the class name
        """
        args = shlex.split(arg)
        if not arg:
            print([str(value) for value in models.storage.all().values()])
        elif args[0] not in models.classes:
            print("** class doesn't exist **")
        else:
            print([str(value) for key, value in models.storage.all().items()
                   if key.split('.')[0] == args[0]])

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id
        by adding or updating attribute
        """
        args = shlex.split(arg)
        if not arg:
            print("** class name missing **")
        elif args[0] not in models.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            key = args[0] + "." + args[1]
            if key not in models.storage.all():
                print("** no instance found **")
            else:
                setattr(models.storage.all()[key], args[2], args[3])
                models.storage.save()


if __name__ == '__main__':
    """
    Main function
    """
    HBNBCommand().cmdloop()
