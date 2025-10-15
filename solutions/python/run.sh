for dir in */; do
  if [ -d "$dir" ]; then
    # Remove the trailing slash from the directory name for cleaner output if needed
    dirname_clean="${dir%/}"
    echo "$dirname_clean"
    # Execute your command, using "$dirname_clean" for the directory name
    # Example: List contents of the directory
#    (cd "$dir" && ls -l)
    (findimports "$dir" --csv 2>&1 | sed 's/^/    /')
    # Example: You can also use the directory name in the command directly:
    # echo "This is $dirname_clean" >> "$dirname_clean/log.txt"
  fi
done

# run.sh > modules.csv