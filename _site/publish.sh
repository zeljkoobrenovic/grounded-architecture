cd manuscript/scripts
python3 copy-and-update-posts.py
cd ../..
git add .
git commit -m "publishing changes"
git push
