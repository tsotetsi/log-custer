#!/usr/bin/env python

import sys
import os

from config import app_logs_dir, app_log_file_name

def main():
	pass

def tail():
	command = "cd "+app_logs_dir+" && tail -F "+app_log_file_name
	return command

if __name__ == '__main__':
	main()