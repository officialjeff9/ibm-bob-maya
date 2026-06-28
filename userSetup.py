import maya.cmds as cmds
import os

# 1. ALWAYS open the door so the background watcher can talk to Maya
if not cmds.commandPort(name=':9006', q=True):
    cmds.commandPort(name=':9006', sourceType='python')
    print(">>> Maya command port 9006 is open and waiting.")