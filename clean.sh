# use this for cleaning the frames removing undesired symbols

for filename in ./*; do
    cat $filename | sed 's/`/ /g' | sed 's/-/ /g' | sed 's/\./ /g' | sed 's/:/ /g' > $filename
done
