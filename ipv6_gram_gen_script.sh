main_dir=$(dirname "$(realpath "$0")")  # brew install coreutils / sudo apt install coreutils

echo "$main_dir"

grammarinator-process ipv6/ipv6.g4 -o ipv6/

grammarinator-generate ipv6Generator.ipv6Generator  -r start -o tests/ipv6/test_%d.txt -n 10 --sys-path $main_dir/ipv6


