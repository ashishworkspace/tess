# CI/CD
### <strong>Precily DevOps Task</strong>

Step 1: Clone the repo
```bash 
git clone git@github.com:ashishworkspace/tess.git 
``` 
Step 2: Build the image 
```bash
cd tess
docker build -t flask_ocr .
```
Step 3: Run the docker container 
```bash
docker run -d -p 5000:4000 flask_ocr 
```
Step 4: Now test the endpoint => Hit to url i.e. GET request 👇
```bash
http://localhost:5000
```
Step 5: POST the request to endpoint =>  /read_ocr 
```bash
curl --location --request POST 'http://localhost:5000/read_ocr' \
--header 'Content-Type: application/json' \
--data-raw '{
    "image": "https://pe-images.s3.amazonaws.com/type/effects/image-in-text/new/photoshop-image-in-text.jpg",
    "lang": "eng",
    "config": "--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789"
}'
```
