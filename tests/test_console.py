#!/user/bin/python3
"""This is the test for the interpreter(console.py) file,
testing the filestorage class"""

import unittest
import json
import pep8
import os
from io import stringIO
from unittest.mock import patch
from console import HBNBCommand
from models.engine.file_storage import FileStorage


class TestConsoleFile(unittest.TestCase):
    """Test for console.py"""
    maxDiff = None

    def setUp(self):
        """File saving testing condition"""
        with open("test.json", 'w'):
            FileStorage._FileStorage__file_path = "test.json"
            FileStorage._FileStorage__objects = {}

    def tearDown(self):
        """discards created files"""
        FileStorage._FileStorage__file_path = "file.json"
        try:
            os.removed("test.json")
        except FileNotFoundError:
            pass

    def test_module_documentation(self):
        """Checks if module is documented"""
        self.assertTrue(len(HBNBCommand.__doc__) > 0)

    def test_class_documentation(self):
        """Checks for console class documentation"""
        self.assertTrue(len(HBNBCommand.__doc__) > 0)

    def test_method_documentattion(self):
        """checks for method documentation"""
        for funcs in dir(HBNBCommand):
            self.assertTrue(len(funcs.__doc__) > 0)

    def test_for_pep8(self):
        """test both console.py and its test file for conformance to pep8"""
        style_guide = pep8.StyleGuide(quiet=True)
        file_1 = 'console.py'
        file_2 = 'tests/test_console.py'
        check_result = style.check_files([file1, file2])
        self.assertEqual(check_result.total_errors, 0,
                         "Code style errors found (and warning).")

    def test_excecutable_file(self):
        """Check if file have the permission to execute"""
        # Checks for read permission
        is_read_on = os.access('console.py', os.R_OK)
        self.assertTrue(is_read_on)
        # Checks for write permission
        is_write_on = os.access('console.py', os.W_OK)
        self.assertTrue(is_write_on)
        # check for excecute permission
        is_exec_on = os.access('console.py', os.X_OK)
        self.assertTrue(is_exec_on)

    def test_help_check(self):
        """checks that each command has help doc"""
        with patch('sys.stdout', new=StringIO()) as help_doc:
            HBNBCommand().onecmd("help create")
            self.assertTrue(len(help_doc.getvalue()) > 0)

        with patch('sys.stdout', new=StringIO()) as help_doc:
            HBNBCommand().onecmd("help all")
            self.assertTrue(len(help_doc.getvalue()) > 0)

        with patch('sys.stdout', new=StringIO()) as help_doc:
            HBNBCommand().onecmd("help show")
            self.assertTrue(len(help_doc.getvalue()) > 0)

        with patch('sys.stdout', new=StringIO()) as help_doc:
            HBNBCommand().onecmd("help destroy")
            self.assertTrue(len(help_doc.getvalue()) > 0)

        with patch('sys.stdout', new=StringIO()) as help_doc:
            HBNBCommand().onecmd("help update")
            self.assertTrue(len(help_doc.getvalue()) > 0)

    def test_create_working_good(self):
        """Test the create method"""
        with patch('sys.stdout', new=StringIO()) as help_doc:
            HBNBCommand().onecmd("create BaseModel")
            self.assertTrue(len(help_doc.getvalue()) > 0)

    def test_create_empty(self):
        """Test to check if create method is empty"""
        with patch('sys.stdout', new=StringIO()) as help_d:
            HBNBCommand().onecmd("create")
            self.assertEqual(help_d.getvalue(), "** class name missing **\n")

    def test_create_unknown(self):
        """Test to check if create can get value"""
        with patch('sys.stdout', new=StringIO()) as v:
            HBNBCommand().onecmd("create Holberton")
            self.assertEqual(v.getvalue(), "** class doesn't exist **\n")

    def test_show_method(self):
        """Test show with normal param"""
        with patch('sys.stdout', new=StringIO()) as value:
            HBNBCommand().onecmd('create BaseModel')
            base_model_id = value.getvalue()
            self.assertTrue(len(base_model_id) > 0)
        with patch('sys.stdout', new=StringIO()) as value:
            HBNBCommand().onecmd('show BaseModel ' + base_model_id)
            self.assertTrue(value.getvalue() != "** no instance found **\n")

    def test_not_found_show_method(self):
        """Test show method with class that does not exist"""
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('show study ')
            self.assertTrue(val.getvalue() == "** class doesn't exist **\n")

    def test_show_is_empty(self):
        """Test show with no class argument(first arg)"""
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('show')
            self.assertTrue(val.getvalue() == "** class name missing **\n")

    def test_show_id(self):
        """Test show with missing 'id'"""
        with patch('sys.stdout', new=StringIO()) as value:
            HBNBCommand().onecmd('show BaseModel')
            self.assertTrue(value.getvalue() == "** instance id missing **\n")

    def test_if_destroy_empty(self):
        """Checks if class(as argument) is missing"""
        with patch('sys.stdout', new=StringIO()) as v:
            HBNBCommand().onecmd('destroy')
            self.assertTrue(v.getvalue() == "** class name missing **\n")

    def test_destroy_invalid_class(self):
        """Checks if class name (as argument) does not exist"""
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('destroy Invalidclass')
            self.assertTrue(val.getvalue() == "** class doesn't exist **\n")

    def test_destroy_id(self):
        """Check if the id is deleted"""
        with patch('sys.stdout', new=StringIO()) as v:
            HBNBCommand().onecmd('destroy BaseModel')
            self.assertTrue(v.getvalue() == "** instance id missing **\n")

    def test_destroy_not_found(self):
        """Checks if the 'id' belongs to an instance"""
        with patch('sys.stdout', new=StringIO()) as v:
            HBNBCommand().onecmd('create BaseModel')
        with patch('sys.stdout', new=StringIO()) as v:
            HBNBCommand().onecmd('destroy BaseModel 0220288')
            self.assertTrue(v.getvalue() == "** no instance found **\n")

    def destroy_instance(self):
        """Checks if destroy method successffully deletes
        an instance """
        with patch('sys.stdout', new=StringIO()) as v:
            HBNBCommand().onecmd('create BaseModel')
            base_model_id = v.getvalue()
            self.assertTrue(len(basemodel_id) > 0)

        with patch('sys.stdout', new=StringIO()) as v:
            HBNBCommand().onecmd('destroy BaseModel ' + basemodel_id)
            self.assertTrue(v.getvalue() != "** no instance found **\n")

    def test_all_invalid_class(self):
        """Checks if class exist"""
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('create BaseModel')
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('all Invalidclass')
            self.assertTrue(val.getvalue() == "** class doesn't exist **\n")

    def test_all_working_class(self):
        """ Checks if the method all works accurately"""
        with patch('sys.stdout', new=StringIO()) as v:
            HBNBCommand().onecmd('create BaseModel')
        with patch('sys.stdout', new=StringIO()) as v:
            HBNBCommand().onecmd('all')
            self.assertTrue(len(v.getvalue()) > 0)

    def test_all_valid_class(self):
        """Check that all methods work accurately with a class arg"""
        with patch('sys.stdout', new=StringIO()) as v:
            HBNBCommand().onecmd('create BaseModel')
        with patch('sys.stdout', new=StringIO()) as v:
            HBNBCommand().onecmd('all BaseModel')
            self.assertTrue(len(val.getvalue()) > 0)

    def test_update_if_class_missing(self):
        """Checks if class arg is missing"""
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('update')
            self.assertTrue(val.getvalue() == "** class name missing **\n")

    def test_update_the_wrong_class(self):
        """Checks if arg class exist"""
        with patch('sys.stdout', new=StringIO()) as v:
            HBNBCommand().onecmd('create BaseModel')
            with patch('sys.stdout', new=StringIO()) as v:
                HBNBCommand().onecmd('update InvalidClass')
                self.assertTrue(v.getvalue() == "** class doesn't exist **\n")

    def test_update_no_instance_id(self):
        """check if the instance of is missing"""
        with patch('sys.stdout', new=StringIO()) as v:
            HBNBCommand().onecmd('create BaseModel')
            with patch('sys.stdout', new=StringIO()) as v:
                HBNBCommand().onecmd('update BaseModel')
                self.assertTrue(v.getvalue() == "** instance id missing **\n")

    def test_update_not_found_id(self):
        """Checks if instance 'id' exits"""
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('create BaseModel')
            with patch('sys.stdout', new=StringIO()) as val:
                HBNBCommand().onecmd('update BaseModel 0220288')
                self.assertTrue(val.getvalue() == "** no instance found **\n")

    def test_update_missing_name_arg(self):
        """Check if name atrr is mising"""
        with patch('sys.stdout', new=StringIO()) as class_id:
            HBNBCommand().onecmd('create BaseModel')
            basemodel_id = class_id.getvalue()
            self.assertTrue(len(base_model_id) > 0)
        with patch('sys.stdout', new=StringIO()) as v:
            HBNBCommand().onecmd('update BaseModel ' + base_model_id)
            self.assertTrue(v.getvalue() == "** attribute name missing **\n")

    def test_update_missing_value(self):
        """Checks ifff attr value is missing"""
        with patch('sys.stdout', new=StringIO()) as class_id:
            HBNBCommand().onecmd('create BaseModel')
            base_model_id = class_id.getvalue()
            self.assertTrue(len(base_model_id) > 0)
        with patch('sys.stdout', new=StringIO()) as v:
            HBNBCommand().onecmd('update BaseModel '
                                 + base_model_id + "first_name")
            self.assertTrue(v.getvalue() == "** value missing **\n")

    def test_update_working(self):
        """test if update is working accurately"""
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd("create BaseModel")
            my_id = val.getvalue()
        with patch('sys.stdout', new=StringIO()) as val:
            BNBCommand().onecmd("update BaseModel " + my_id + " name betty")
            HBNBCommand().onecmd("show BaseModel " + my_id)
            self.assertTrue("betty" in val.getvalue())

    def test_update_ok_accurate(self):
        """update tast worked"""
        with patch('sys.stdout', new=StringIO()) as v:
            HBNBCommand().onecmd("create BaseModel")
            u_id = v.getvalue()
        with patch('sys.stdout', new=StringIO()) as v:
            HBNBCommand().onecmd("update BaseModel " + u_id + " name misy hi")
            self.assertTrue("betty" in v.getvalue())

    def test_clas_user_with_console(self):
        """ Test the class user with console """
        with patch('sys.stdout', new=StringIO()) as v:
            HBNBCommand().onecmd("create User")
            u_id = v.getvalue()
            self.assertTrue(u_id != "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as v:
            HBNBCommand().onecmd("show User " + u_id)
            self.assertTrue(v.getvalue() != "** no instance found **\n")
        with patch('sys.stdout', new=StringIO()) as v:
            HBNBCommand().onecmd("all User")
            self.assertTrue(v.getvalue() != "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as v:
            HBNBCommand().onecmd("update User " + u_id + " name betty")
            HBNBCommand().onecmd("show User " + u_id)
            self.assertTrue("missy" in v.getvalue())
            HBNBCommand().onecmd("destroy User " + u_id)
        with patch('sys.stdout', new=StringIO()) as v:
            HBNBCommand().onecmd("show User " + u_id)
            self.assertEqual(v.getvalue(), "** no instance found **\n")

    def test_place_method_of_class_user_with_console(self):
        """ Test the class user 'place' method with console """
        with patch('sys.stdout', new=StringIO()) as v:
            HBNBCommand().onecmd("create Place")
            u_id = v.getvalue()
            self.assertTrue(u_id != "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd("show Place " + u_id)
            self.assertTrue(val.getvalue() != "** no instance found **\n")
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd("all Place")
            self.assertTrue(val.getvalue() != "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as v:
            HBNBCommand().onecmd("update Place " + u_id + " name betty")
            HBNBCommand().onecmd("show Place " + u_id)
            self.assertTrue("missy" in v.getvalue())
            HBNBCommand().onecmd("destroy Place " + u_id)
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd("show Place "+u_id)
            self.assertEqual(val.getvalue(), "** no instance found **\n")

    def test_state_console(self):
        """ Test the class user with console """
        with patch('sys.stdout', new=StringIO()) as v:
            HBNBCommand().onecmd("create State")
            u_id = v.getvalue()
            self.assertTrue(u_id != "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as v:
            HBNBCommand().onecmd("show State " + u_id)
            self.assertTrue(v.getvalue() != "** no instance found **\n")
        with patch('sys.stdout', new=StringIO()) as v:
            HBNBCommand().onecmd("all State")
            self.assertTrue(v.getvalue() != "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as v:
            HBNBCommand().onecmd("update State " + u_id + " name betty")
            HBNBCommand().onecmd("show State " + u_id)
            self.assertTrue("betty" in v.getvalue())
            HBNBCommand().onecmd("destroy State " + u_id)
        with patch('sys.stdout', new=StringIO()) as v:
            HBNBCommand().onecmd("show State "+u_id)
            self.assertEqual(v.getvalue(), "** no instance found **\n")

    def test_city_console(self):
        """ Test the class user method 'city' with console """
        with patch('sys.stdout', new=StringIO()) as v:
            HBNBCommand().onecmd("create City")
            u_id = v.getvalue()
            self.assertTrue(u_id != "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd("show City " + u_id)
            self.assertTrue(val.getvalue() != "** no instance found **\n")
        with patch('sys.stdout', new=StringIO()) as v:
            HBNBCommand().onecmd("all City")
            self.assertTrue(v.getvalue() != "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as v:
            HBNBCommand().onecmd("update City " + u_id + " name betty")
            HBNBCommand().onecmd("show City " + u_id)
            self.assertTrue("betty" in v.getvalue())
            HBNBCommand().onecmd("destroy City " + u_id)
        with patch('sys.stdout', new=StringIO()) as v:
            HBNBCommand().onecmd("show City "+u_id)
            self.assertEqual(v.getvalue(), "** no instance found **\n")

    def test_clas_user_amenity_console(self):
        """ Test the class user 'amenity' method with console """
        with patch('sys.stdout', new=StringIO()) as v:
            HBNBCommand().onecmd("create Amenity")
            u_id = v.getvalue()
            self.assertTrue(u_id != "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as v:
            HBNBCommand().onecmd("show Amenity " + u_id)
            self.assertTrue(v.getvalue() != "** no instance found **\n")
        with patch('sys.stdout', new=StringIO()) as v:
            HBNBCommand().onecmd("all Amenity")
            self.assertTrue(v.getvalue() != "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd("update Amenity " + u_id + " name betty")
            HBNBCommand().onecmd("show Amenity " + u_id)
            self.assertTrue("betty" in val.getvalue())
            HBNBCommand().onecmd("destroy Amenity " + u_id)
        with patch('sys.stdout', new=StringIO()) as v:
            HBNBCommand().onecmd("show Amenity "+u_id)
            self.assertEqual(v.getvalue(), "** no instance found **\n")

    def test_review_method_with_console(self):
        """ Test the class user 'Review' method with console """
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd("create Review")
            u_id = val.getvalue()
            self.assertTrue(user_id != "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd("show Review " + u_id)
            self.assertTrue(val.getvalue() != "** no instance found **\n")
        with patch('sys.stdout', new=StringIO()) as v:
            HBNBCommand().onecmd("all Review")
            self.assertTrue(v.getvalue() != "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd("update Review " + u_id + " name betty")
            HBNBCommand().onecmd("show Review " + u_id)
            self.assertTrue("missy" in val.getvalue())
            HBNBCommand().onecmd("destroy Review " + u_id)
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd("show Review "+u_id)
            self.assertEqual(val.getvalue(), "** no instance found **\n")

    def test_alternative_all_method_in_user(self):
        """test alternative all with the key [class].all"""
        with patch('sys.stdout', new=StringIO()) as value:
            HBNBCommand().onecmd("create User")
        with patch('sys.stdout', new=StringIO()) as value:
            HBNBCommand().onecmd("User.all()")
            self.assertTrue(len(value.getvalue()) > 0)

    def test_show_method_alternative(self):
        """test alt show with the key [class].show"""
        with patch('sys.stdout', new=StringIO()) as value:
            HBNBCommand().onecmd("create User")
            u_id = value.getvalue()
        with patch('sys.stdout', new=StringIO()) as value:
            HBNBCommand().onecmd("User.show(\"" + u_id + "\")")
            self.assertTrue(len(value.getvalue()) > 0)

    def test_the_count_method(self):
        """test the count method"""
        with patch('sys.stdout', new=StringIO()) as value:
            HBNBCommand().onecmd("User.count()")
            self.assertTrue(int(value.getvalue()) == 0)
        with patch('sys.stdout', new=StringIO()) as value:
            HBNBCommand().onecmd("create User")
        with patch('sys.stdout', new=StringIO()) as value:
            HBNBCommand().onecmd("User.count()")
            self.assertTrue(int(value.getvalue()) == 1)

    def test_destroy_method_alternative(self):
        """test the alternative destroy method with example:
            [class].destroy(id)"""
        with patch('sys.stdout', new=StringIO()) as value:
            HBNBCommand().onecmd("create User")
            u_id = value.getvalue()
        with patch('sys.stdout', new=StringIO()) as value:
            HBNBCommand().onecmd("User.destroy(\"" + u_id + "\")")
        with patch('sys.stdout', new=StringIO()) as value:
            HBNBCommand().onecmd("User.count()")
            self.assertTrue(int(value.getvalue()) == 0)

    def test_first_alternative_update(self):
        """test alternative update with [class].show"""
        with patch('sys.stdout', new=StringIO()) as value:
            HBNBCommand().onecmd("create User")
            u_id = value.getvalue()
        with patch('sys.stdout', new=StringIO()) as value:
            line_args = "\", \"name\", \"missy\")"
            HBNBCommand().onecmd("User.update(\"" + u_id + line_args)
        with patch('sys.stdout', new=StringIO()) as value:
            HBNBCommand().onecmd("User.show(\"" + u_id + "\")")
            self.assertTrue("missy" in value.getvalue())

    def test_second_alternative_update(self):
        """test test the alternative update with the command:
            [class].show"""
        with patch('sys.stdout', new=StringIO()) as value:
            HBNBCommand().onecmd("create User")
            u_id = val.getvalue()
        with patch('sys.stdout', new=StringIO()) as value:
            line_args = "\", {'first_name': 'missy', 'age': 31})"
            HBNBCommand().onecmd("User.update(\"" + u_id + line_args)
        with patch('sys.stdout', new=StringIO()) as value:
            HBNBCommand().onecmd("User.show(\"" + u_id + "\")")
            self.assertTrue("missy" in value.getvalue())


if __name__ == '__main__':
    unittest.main()
