#!/bin/bash


cd /home/larry/note/

git pull origin master

cd /home/larry/github/autoNote/
python autoNote.py

cd /home/larry/note/
git add -A

cd /home/larry/note/
git commit -m'add note'

cd /home/larry/note/
git push origin master

year=`date -d now +%Y`
mouth=`date -d now +%m`
day=`date -d now +%d`
time=`date -d now +%Y-%m-%d`

chromium-browser https://github.com/Pioneer-Linzi/mynote/tree/master/log/${year}/${mouth}/${time}.md


