#!/bin/bash

python3 -m src.main \
    --vfs "./test-vfs-2.csv" \
    --prompt "shell-2$ " \
    --script "./scripts/startup.sh"