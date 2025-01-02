#!/bin/bash
set -e

# Build the package
python3 -m build

# Files are already in dist/ directory by default
# No need to move them
