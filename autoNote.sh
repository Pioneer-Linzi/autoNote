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

year=`date +%Y`
mouth=`date  +%m`
day=`date  +%d`
time=`date +%Y-%m-%d`
open -a Google\ Chrome https://github.com/Pioneer-Linzi/mynote/tree/master/log/${year}/${mouth}/${time}.md


