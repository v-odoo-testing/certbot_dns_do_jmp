#!/bin/bash
set -e

# Build the package
python3 -m build

# Create dist directory if it doesn't exist
mkdir -p dist

# Move built packages to dist directory
mv *.whl dist/
mv *.tar.gz dist/
