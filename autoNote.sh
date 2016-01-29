#!/bin/bash

python autoNote.py

cd /home/linzi/note/

git pull origin master

git add -A

git commit -m'add note'

git push origin master

year=`date -d now +%Y`
mouth=`date -d now +%m`
day=`date -d now +%d`
time=`date -d now +%Y-%m-%d`

chromium-browser https://github.com/Pioneer-Linzi/mynote/tree/master/log/${year}/${mouth}/${time}.md


