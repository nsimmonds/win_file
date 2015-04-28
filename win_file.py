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
      - Absolute path to the file location.
      - Alternatively, just a filename if mkdir
      - is present
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
      - Optional directory to create. If present,
      - will always attempt to create the directory.
      - Use when unsure whether the directory exists.
      - If mkdir is present, it is assumed that file
      - is just a filename
      - Include trailing slashes
    required: false
    default: null
    aliases: []
'''
