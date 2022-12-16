### Building a frontend container for mesh access:

```
docker build -t snpsuen/meshfront:v1 -f Dockerfile .
docker run -d --name meshfront -p 5005:5005 snpsuen/meshfront:
docker login -u snpsuen
docker push snpsuen/meshfront:v1
```
