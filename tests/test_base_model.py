#!/usr/bin/python3
"""Unittests for class path models/base_model.py:
unittest classes:
    TestBaseModel_save
    TestBaseModel_instances
    TestBaseModel_to_dict
"""


import unittest
from models.base_model import BaseModel
import models
from datetime import datetime
import os
from time import sleep


class TestBaseModel_instances(unittest.TestCase):
    """Testing instantiations of the BaseModel class"""

    def test_number_of_arguments(self):
        models_inst = BaseModel()
        self.assertEqual(models_inst, len(BaseModel()))

    def test_new_instance_in_object(self):
        self.assertIn(BaseModel(), models.storage.all().values())

    def test_id_is_stored_as_public_str(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_created_at_is_of_type_datetime(self):
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_updated_at_is_of_type_datetime(self):
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_two_basemodels_inst_unique_ids(self):
        base_inst_1 = BaseModel()
        base_inst_2 = BaseModel()
        self.assertNotEqual(base_inst_1.id, base_inst_2.id)

    def test_time_diff_on_two_model_inst_of_created_at(self):
        base_inst_1 = BaseModel()
        sleep(0.10)
        base_inst_2 = BaseModel()
        self.assertLess(base_inst_1.created_at, base_inst_2.created_at)

    def test_time_diff_on_two_model_inst_of_created_at(self):
        base_inst_1 = BaseModel()
        sleep(0.10)
        base_inst_2 = BaseModel()
        self.assertLess(base_inst_1.updated_at, base_inst_2.updated_at)

    def test_models_str_representation(self):
        d_t = datetime.today()
        repr_d_t = repr(d_t)
        model_inst = BaseModel()
        model_inst.id = "754321"
        model_inst.created_at = model_inst.updated_at = d_t
        model_inst_str = model_inst.__str__()
        self.assertIn("[BasModel] (754321)", model_inst_str)
        self.assertIn("'id': '754321'", model_inst_str)
        self.assertIn("'created_at': " + repr_d_t, model_inst_str)
        self.assertIn("'updated_at': " + repr_d_t, model_inst_str)

    def test_unused_args(self):
        model_inst = BaseModel(None)
        self.assertNotIn(None, models.__dict__.values())

    def test_instances_with_kwargs(self):
        d_t = datetime.today()
        d_t_isoform = d_t.isoformat()
        model_inst = BaseModel(created_at=d_t_isoform,
                               updated_at=d_t_isoform, id="007")
        self.assertEqual(model_inst.id, "007")
        self.assertEqual(model_inst.created_at, d_t)
        self.assertEqual(model_inst.updated_at, d_t)

    def test_instances_with_no_kwargs(self):
        with self.assertRaises(TypeError):
            BaseModel(id=None, created_at=None, updated_at=None)

    def test_instances_with_args_and_kwargs(self):
        d_t = datetime.today()
        d_t_isoform = d_t.isoformat()
        model_inst = BaseModel("89", id="007", created_at=d_t_isoform,
                               updated_at=d_t_isoform)
        self.assertEqual(model_inst.id, "007")
        self.assertEqual(model_inst.created_at, d_t)
        self.assertEqual(model_inst.updated_at, d_t)


class TestBaseModel_save(unittest.TestCase):
    """BaseModel's class test method"""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "temp")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("temp", "file.json")
        except IOError:
            pass

    def test_save_one(self):
        model_inst = BaseModel()
        sleep(0.10)
        first_updated_at = model_inst.updated_at
        model_inst.save()
        self.assertLess(first_updated_at, model_inst.updated_at)

    def test_save_two(self):
        model_inst = BaseModel()
        sleep(0.10)
        first_updated_at = model_inst.updated_at
        model_inst.save()
        second_updated_at = model_inst.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.10)
        model_inst.save()
        self.assertLess(second_updated_at, model_inst.updated_at)

    def test_save_with_args(self):
        model_inst = BaseModel()
        with self.assertRaises(TypeError):
            model_inst.save(None)

    def test_file_updates_with_save(self):
        model_inst = BaseModel()
        model_inst.save()
        model_inst_id = "BaseModel." + model_inst.id
        with open("file.json", "r") as f:
            self.assertIn(model_inst_id, f.read())


class TestBaseModel_to_dict(unittest.TestCase):
    """Testing the BaseModel's to_dict method"""

    def test_type_of_to_dict(self):
        model_inst = BaseModel()
        self.assertTrue(dict, type(model_inst.to_dict()))

    def Test_to_dict_has_correct_keys(self):
        model_inst = BaseModel()
        self.assertIn("id", model_inst.to_dict())
        self.assertIn("created_at", model_inst.to_dict())
        self.assertIn("updated_at", model_inst.to_dict())
        self.assertIn("__class__", model_inst.to_dict())

    def test_to_dict_has_passed_attributes(self):
        model_inst = BaseModel()
        model_inst.name = "ALX"
        model_inst.my_number = "30"
        self.assertIn("name", model_inst.to_dict())
        self.assertIn("my_number", model_inst.to_dict())

    def test_to_dict_datetime_attr_are_strs(self):
        model_inst = BaseModel()
        model_dict = model_inst.to_dict()
        self.assertEqual(str, type(model_dict["created_at"]))
        self.assertEqual(str, type(model_dict["updated_at"]))

    def test_to_dict_output(self):
        d_t = datetime.today()
        model_inst = BaseModel()
        model_inst.id = "754321"
        model_inst.created_at = model_inst.updated_at = d_t
        conv_dict = {
                'id': '754321',
                '__class__': 'BaseModel',
                'created_at': d_t.isoformat(),
                'updated_at': d_t.isoformat()
                }
        self.assertDictEqual(model_inst.to_dict(), conv_dict)

    def test_to_dict_with_args(self):
        model_inst = BaseModel()
        with self.assertRaises(TypeError):
            model_inst.to_dict(None)

    def test_contrast_to_dict_to_dunder_dict(self):
        model_inst = BaseModel()
        self.assertEqual(model_inst.to_dict(), model_inst.__dict__)


if __name__ == "__main__":
    unittest.main()
