for (( ; ; )); do
  curl "https://leanpub.com/groundedarchitecture/job_status?api_key=96FF3A08D7D0443AA6D0C64A73235444" > status.json
  tail status.json

  if grep -o -e "{}" "status.json"; then
    echo "FOUND"
    curl -L "https://leanpub.com/s/B36725C24EB34CBD99A3FB1D71011E61.epub" -o assets/book/groundedarchitecture.epub
    exit
  else
    echo 'the string does not exist'
  fi
  echo "sleeping 10 seconds..."
  sleep 10
done
