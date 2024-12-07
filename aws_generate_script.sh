main_dir=$(dirname "$(realpath "$0")")  # brew install coreutils / sudo apt install coreutils
    
grammarinator-process $main_dir/awsarn/awsarn.g4 -o awsarn/
    
# grammarinator-generate awsarnGenerator.awsarnGenerator  -r start -o tests/awsarn/test_%d.txt -n 10 --sys-path $main_dir/awsarn

grammarinator-generate awsarnGenerator.awsarnGenerator --sys-path $main_dir/awsarn -r awsarn -d 10 -n 5

# grammarinator-generate customUrlGenerator.customUrlGenerator --sys-path $main_dir/url_grammarinator_files -r url -d 10 -n 5