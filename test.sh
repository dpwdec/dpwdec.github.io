change=`git diff --name-only --diff-filter=RAD HEAD^ HEAD`
if [ -z $change ]; then
    echo "hello"
else
    echo "goodbye"
fi
