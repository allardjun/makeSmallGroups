#!/bin/bash

localPathOfM227CRepo="~/git/pub/Math227C/"

cp teams_M227C.svg $localPathOfM227CRepo

cd $localPathOfM227CRepo 
git add .
git commit -m 'groups for today'
git push

