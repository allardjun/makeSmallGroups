#!/bin/bash

rclone sync jallard_uci_gdrive:Notability ~/notability

source /Users/jun/git/pub/makeSmallGroups/venv/bin/activate
python3 /Users/jun/git/pub/makeSmallGroups/makeSmallGroups.py P230
deactivate

source /Users/jun/git/pub/canvas_tools/venv/bin/activate
python /Users/jun/git/pub/canvas_tools/upload_lecture_notes.py
python /Users/jun/git/pub/canvas_tools/upload_small_groups.py
deactivate