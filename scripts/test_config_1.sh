#!/bin/bash

python3 -m src.main \
    --vfs "./test-vfs-1.csv" \
    --prompt "shell-1$ " \
    --script "./scripts/startup.sh"