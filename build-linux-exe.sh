#!/bin/bash
echo "Build Linux executable"
pyxel app2exe kill-the-keys.pyxapp
mkdir -p AppDir/usr/bin
cp kill-the-keys AppDir/usr/bin
echo "Build AppImage"
appimage-builder-1.1.0-x86_64.AppImage
