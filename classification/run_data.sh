#!/usr/bin/env sh

SCRIPT=$(readlink -f "$0")
SCRIPTPATH=$(dirname "$SCRIPT")
LLS=LLS.py

echo "====================================="
echo "Iris Dataset:"
echo "====================================="
$SCRIPTPATH/$LLS data/iris.csv
echo "\n"

echo "====================================="
echo "Wine Dataset:"
echo "====================================="
$SCRIPTPATH/$LLS data/wine.csv --head
echo "\n"

echo "====================================="
echo "Parkinsons Dataset:"
echo "====================================="
$SCRIPTPATH/$LLS data/parkinson.csv
echo "\n"

echo "====================================="
echo "Social Media Dataset:"
echo "====================================="
$SCRIPTPATH/$LLS data/social-media.csv
echo "\n"
