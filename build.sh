#!/bin/bash

if [ ! -d package ]; then mkdir package; fi

echo "Prepare the package"
cp -r main.py assets.pyxres package
cd package
pyxel package . main.py
mv package.pyxapp ../kill-the-keys.pyxapp
cd ..
echo "To HTML"
pyxel app2html kill-the-keys.pyxapp
mv kill-the-keys.html index.html
echo "Clean"
rm -r package
echo "End"