1. source env/bin/activate
2. python Server.py
3. python client.py

contents of sample.txt will be written into resources directory, yes , overwritten


using curl is fine as well

curl \
  -F "userid=1" \
  -F "filecomment=This is an txt file" \
  -F "file=@sample.txt" \
  localhost:8000/file_save