cd manuscript/scripts
python3 copy-and-update-posts.py
python3 make-epub.py
cp -f ../epub/* ../
cd ../..
git add .
git commit -m "publishing changes"
git push
