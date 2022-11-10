# EKS & ALB load testing

- [x] create cluster
- [x] install metrics server
- [ ] Install alb driver
- [x] deploy httpbin
- [ ] deploy load server
- [ ] deploy locust script
- [ ] export test resaults

## Cluster setup

```sh
eksctl create cluster --name eks-alb-demo --region eu-central-1 --full-ecr-access  --nodes-min 3 --spot
```

## install metrics server

```sh
kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml
# then to test
kubectl get deployment metrics-server -n kube-system
```

## Install ALB Network provider

[docs](https://docs.aws.amazon.com/eks/latest/userguide/aws-load-balancer-controller.html)

## Deploy httpbin to cluster

```sh
kubectl create deployment --image=kennethreitz/httpbin --replicas=2 --port=80
```
