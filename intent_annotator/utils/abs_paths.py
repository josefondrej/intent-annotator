import os

THIS_FILE_PATH = os.path.realpath(__file__)
PACKAGE_PATH = "/".join(THIS_FILE_PATH.split("/")[:-2])
RESOURCES_PATH = PACKAGE_PATH + "/files/"