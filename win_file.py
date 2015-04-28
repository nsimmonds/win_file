#!/usr/bin/python

DOCUMENTATION = '''
---
module: win_file
version_added: ""
short_description: File manipulation within Windows
author: Nick Simmonds
description:
     - Creates, moves, edits, deletes, etc.
     - files within Windows via native Powershell
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
  mkdir:
    description:
      - Option directory to create. If present,
      - will always attempt to create the directory.
      - Note that "file" should still be an absolute path
    required: false
    default: null
    aliases: []

'''
