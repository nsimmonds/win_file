#!/usr/bin/python

DOCUMENTATION = '''
---
module: win_file
version_added: ""
short_description: File manipulation within Windows
description:
     - Creates, moves, edits, deletes, etc. files within Windows via native Powershell
options:
  file:
    description:
      - Absolute path to the file location
    required: true
    default: null
    aliases: []
  action:
    description:
      - The file manipulation intended
    required: false
    default: create
    choices: [create, update, delete, move]
    aliases: []
  content:
    description:
      - Intended file content (use with "create" or "update")
    required: false
    default: null
    aliases: []
author: Nick Simmonds
'''
