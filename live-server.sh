#!/bin/bash

set -x -o pipefail

. .venv/bin/activate

sphinx-autobuild --write-all BOOK build/html
