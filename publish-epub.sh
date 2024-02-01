cd manuscript/scripts
python3 copy-and-update-posts.py
python3 make-epub.py
cp -f ../epub/* ../
cd ../..
git add .
git commit -m "publishing changes"
git push

curl -d "api_key=96FF3A08D7D0443AA6D0C64A73235444" https://leanpub.com/groundedarchitecture/preview.json
curl "https://leanpub.com/groundedarchitecture.json?api_key=96FF3A08D7D0443AA6D0C64A73235444" > info.json