#!/bin/bash


cd ~/note/mynote

git pull origin master

cd ~/note/autoNote/
python autoNote.py

cd ~/note/mynote
git add -A

cd ~/note/mynote
git commit -m'add note'

cd ~/note/mynote
git push origin master

year=`date -d now +%Y`
mouth=`date -d now +%m`
day=`date -d now +%d`
time=`date -d now +%Y-%m-%d`

google-chrome https://github.com/Pioneer-Linzi/mynote/tree/master/log/${year}/${mouth}/${time}.md


