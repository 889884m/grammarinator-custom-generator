
main_dir=$(dirname "$(realpath "$0")")  
grammarinator-process ipv6.g4 -o "$main_dir"
grammarinator-generate ipv6Generator.ipv6Generator -r start -o "tests/grammarinator_output/test_%d.txt" -n 500000 --sys-path "$main_dir"