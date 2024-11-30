main_dir=$(dirname "$(realpath "$0")")  # brew install coreutils / sudo apt install coreutils

grammarinator-process $main_dir/url_grammarinator_files/url.g4

grammarinator-generate urlGenerator.urlGenerator --sys-path $main_dir/url_grammarinator_files -r url -d 10 -n 5

grammarinator-generate customUrlGenerator.customUrlGenerator --sys-path $main_dir/url_grammarinator_files -r url -d 10 -n 5


