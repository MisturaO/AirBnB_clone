#!/usr/bin/python3
"""The entry point of the command interpreter"""
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """The command processor class definition:
        class attr:
            prompt(str): The command prompt"""

    prompt = '(hbnb) '
    __valid_classes = ["BaseModel"]

    def do_quit(self, line):
        """'quit' command to exit the program"""
        return True

    def do_EOF(self, line):
        """If EOF arg is indicated this method returns 'True'
        e.g if Ctr-D is passed to the line arg from the keyboard:
            EOF command to exit the program"""
        return True

    def emptyline(self):
        """Overrides the cmd class emptyline method, so that an
        empty line + ENTER wouldn’t execute anything"""
        pass

    def do_create(self, line):
        commands = line.split()
        if commands[0] == "":
            print("** class name missing **")
        elif commands[0] not in self.__valid_classes:
            print("** class doesn't exist **")
        else:
            if commands[0] == "BaseModel":
                new_inst = BaseModel()
                print("{}".format(new_inst.id))


if __name__ == "__main__":
    HBNBCommand().cmdloop()
