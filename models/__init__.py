#!/usr/bin/python3
""" This module initialiazes the models package and contains the
filestorage instance for our application"""

from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
