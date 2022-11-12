# EKS & ALB load testing

- [x] create cluster
- [x] install metrics server
- [ ] Install alb driver
- [x] deploy httpbin
- [ ] Install k6
- [ ] deploy load server
- [ ] deploy locust script
- [ ] export test resaults

## Cluster setup

```sh
eksctl create cluster --name httpbin --region eu-west-2 --full-ecr-access --fargate
```

## install metrics server

```sh
kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml

kubectl get deployment metrics-server -n kube-system
```

## Install ALB Network provider

[docs](https://docs.aws.amazon.com/eks/latest/userguide/aws-load-balancer-controller.html)

## Deploy httpbin to cluster

```sh
kubectl create deployment --image=kennethreitz/httpbin --replicas=2 --port=80
```

## Running k6 test
```sh
k6 run --vue=50 --time=5m script.js
```