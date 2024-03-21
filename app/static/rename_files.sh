### usage: ./rename_files.sh source_folder output_folder initial_count
### example: ./rename_files.sh source IMAGES 0

directory=$1

mkdir $2

count=$3
for file in "$directory"/*;do
    echo $file to $count.jpg [ok]
    cp "$file" $2/$count.jpg
    count=$(echo "$count+1" | bc)
done
