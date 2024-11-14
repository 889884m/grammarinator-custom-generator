#!/bin/bash

set -e

read -p "Create the URL generator with Grammarinator? "
set -x
grammarinator-process url.g4
set +x

read -p "Generate random URLs for testing? (limited subdomains) "
set -x
grammarinator-generate urlGenerator.urlGenerator \
    --sys-path . \
    -r url \
    -d 10 \
    -n 10 \
    -o tests/test_%d.txt
set +x

read -p "Generate random URLs for testing? (expanded subdomains) "
set -x
grammarinator-generate customUrlGenerator.customUrlGenerator \
    --sys-path . \
    -r url \
    -d 10 \
    -n 10 \
    -o custom_tests/test_%d.txt
set +x
