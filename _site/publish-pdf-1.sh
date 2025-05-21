cd manuscript/scripts
python3 copy-and-update-posts.py
cd ../..

cp manuscript/Book1.txt manuscript/Book.txt

git add .
git commit -m "publishing changes"
git push


curl -d "api_key=96FF3A08D7D0443AA6D0C64A73235444" https://leanpub.com/groundedarchitecture/preview.json

for (( ; ; )); do
  curl "https://leanpub.com/groundedarchitecture/job_status?api_key=96FF3A08D7D0443AA6D0C64A73235444" > status.json
  tail status.json

  if grep -o -e "{}" "status.json"; then
    echo "FOUND"
    curl -L "https://leanpub.com/s/B36725C24EB34CBD99A3FB1D71011E61.pdf" -o assets/book/groundedarchitecture-part-1.pdf
    git add .
    git commit -m "publishing changes"
    git push
    open assets/book/groundedarchitecture.pdf
    exit
  else
    echo 'the string does not exist'
  fi
  echo "sleeping 10 seconds..."
  sleep 10
done
