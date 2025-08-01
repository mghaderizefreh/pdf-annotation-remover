#!/usr/bin/env python
import os
import sys

def main():
 os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project_name.settings')
 try:
  from django.core.management import execute_from_command_line
 except ImportError as exc:
  raise ImportError(
   "Couldn't import Django. Make sure it's installed and available on your PYTHONPATH environment variable and that you have activated a virtual environment."
  ) from exc
 execute_from_command_line(sys.argv)

if __name__ == '__main__':
 main()
