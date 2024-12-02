
main_dir=$(dirname "$(realpath "$0")")  
grammarinator-process ipv6.g4 -o ipv6/
grammarinator-generate ipv6Generator.ipv6Generator -r start -o "tests/grammarinator_output/test_0.txt" -n 1 --sys-path "$main_dir"