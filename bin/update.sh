#!/bin/sh

pip uninstall sconfig
if [ "$1" = "-g" -o "$1" = "--git" ]; then
    pip install git+https://github.com/tkosht/simple_config.git
else
    pip install -e .
fi

