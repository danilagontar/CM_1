#!/bin/bash

python3 -m src.main \
    --vfs "./test-vfs-3.csv" \
    --prompt "shell-3$ " \
    --script "./scripts/startup.sh"