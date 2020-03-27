### @package Config file for the Gerrit App """
import os

# Statement for enabling the development environment
DEBUG = True

# Port Number
PORT_NO = 8081

# The Host IP
HOST = '0.0.0.0'

# Define the application directory
basedir = os.path.abspath(os.path.dirname(__file__))
