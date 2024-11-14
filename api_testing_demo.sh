#!/bin/bash

set -e

read -p "Create the API URL generator with Grammarinator? "

set -x
cd api_testing || exit 2
grammarinator-process url.g4
cd -
set +x

read -p "Generate random API URLs for testing? "

set -x
grammarinator-generate api_testing.apiUrlGenerator.ApiUrlGenerator \
    --sys-path . \
    -r url \
    -d 10 \
    -n 20 \
    -o api_tests/test_%d.txt
set +x
