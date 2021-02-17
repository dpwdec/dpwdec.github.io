if [ -z `git diff --name-only --diff-filter=RAD HEAD^ HEAD` ]; then
    echo "hello"
else
    echo "goodbye"
fi
