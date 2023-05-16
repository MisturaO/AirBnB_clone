#!/usr/bin/python3
"""The entry point of the command interpreter"""
import cmd
from models.base_model import BaseModel
from models import storage
from datetime import datetime


class HBNBCommand(cmd.Cmd):
    """The command processor class definition:
        class attrs:
            prompt(str): The command prompt"""

    prompt = '(hbnb) '
    __valid_classes = ["BaseModel", "User"]

    def do_quit(self, line):
        """'quit' command to exit the program"""
        return True

    def do_EOF(self, line):
        """If EOF argument is indicated this method returns 'True'
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

    def do_show(self, line):
        """
        Prints the string representation of an instance based on
        the class name and id. Ex:
        $ show BaseModel 1234-1234-1234.
        """
        args = line.split(" ")
        if len(args) == 0:
            print("** class name missing **")
        if args[0] in self.__valid_classes:
            if len(args) > 1:
                key = args[0] + "." + args[1]
                all_objects = storage.all()
                for k in all_objects.keys():
                    if k == key:
                        print(all_objects[k])
                        break
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id
        (save the change into the JSON file). Ex:
            $ destroy BaseModel 1234-1234-1234."""
        args = line.split(" ")
        if len(args) == 1:
            print("** class name missing **")
        elif args[0] in self.__valid_classes:
            if len(args) > 1:
                key = args[0] + "." + args[1]
                all_objects = storage.all()
                if key in all_objects:
                    del all_objects[key]
                    storage.save()
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_all(self, line):
        """Prints all string representation of all instances
        based or not on the class name. Ex:
            $ all BaseModel or $ all"""
        args = line.split(" ")
        all_objects = []
        if len(args) == 0:
            for val in storage.all().values():
                all_objects.append(str(val))
            print("[", end="")
            print(", ".join(all_objects), end="")
            print("]")
        elif args[0] in self.__valid_classes:
            for key in storage.all():
                if args[0] in key:
                    all_objects.append(str(storage.all()[key]))
            print("[", end="")
            print(", ".join(all_objects), end="")
            print("]")
        else:
            print("** class doesn't exist **")

    def do_update(self, line):
        """Updates an instance based on the class name and id
        by adding or updating attribute"""
        args = line.split(" ")
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] in self.__valid_classes:
            if len(args) < 2:
                print("** instance id missing **")
            key = args[0] + "." + args[1]
            all_objects = storage.all()
            if key not in all_objects:
                print("** no instance found **")
            else:
                object_k = all_objects[key]
                invalid_attrs = ["id", "created_at", "updated_at"]
                if object_k:
                    obj = line.split(" ")
                    if len(obj) < 3:
                        print("** attribute name missing **")
                    elif len(obj) < 4:
                        print("** value missing **")
                    elif obj[2] not in invalid_attrs:
                        object_k.__dict__[obj[2]] = obj[3]
                        object_k.updated_at = datetime.now()
                        storage.save()
        else:
            print("** class doesn't exist **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
