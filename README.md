# CI/CD 

## Docker
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

<br />
<br />

## Kubernetes

Step 1: Run the Kube Manifest file  ( Make sure that minikube is up )

```bash
kubectl apply -f k8s/
```
Step 2: Now check the svc => will return NodePort 
```bash
kubectl get svc -n precily
```
Step 3: Get the minikube ip 
```bash
minikube ip  
```
Step 4: Now run the app
```bash
http://<minikube-ip>:<node-port>
```
Note:
> Image at docker-hub  <br />
> name: `ashishizofficial/flask_ocr:tess`


<br />
<br />

## Github action 

Workflow has mainly 2 steps.<br />
1st step will build the docker image and push the docker image to docker hub public reg.<br />
2nd step will deploy the kubernetes manifest file will latest image & tag.<br />

### Script present at server => `script.sh`
```bash
#!/bin/bash

cd /home/ec2-user/precily/tess/
git pull
export TAG=$(git rev-list HEAD --max-count=1)

#Kubernetes manifest
sed  's@ashishizofficial/flask_ocr:tess@'"ashishizofficial/api-flask:tess-$TAG"'@' k8s/app.yml > /home/ec2-user/deploy.yml
kubectl apply -f /home/ec2-user/deploy.yml
```


