# EKS & ALB load testing

- [x] create cluster
- [x] install metrics server
- [x] enable logging to cloudwatch
- [x] create oidc
- [x] create serviceaccount
- [x] Install alb driver
- [x] deploy httpbin
- [x] Install k6
- [x] deploy load server
- [x] deploy locust script
- [ ] export test resaults

## Cluster setup

```sh
eksctl create cluster --name httpbin --region eu-central-1 --full-ecr-access --fargate
```

## install metrics server

```sh
kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml

kubectl get deployment metrics-server -n kube-system
```

## CloudWatch logging

```sh
eksctl utils update-cluster-logging --enable-types all
```

## Create oidc

```sh
eksctl utils associate-iam-oidc-provider --region=eu-central-1 --cluster=demo --approve
```

## create serviceaccount

```sh
eksctl create iamserviceaccount \
  --cluster=demo \
  --namespace=kube-system \
  --name=aws-load-balancer-controller \
  --role-name "AmazonEKSLoadBalancerControllerRole" \
  --attach-policy-arn=arn:aws:iam::<my aws id >:policy/AWSLoadBalancerControllerIAMPolicy \
  --approve
```

## Install ALB Network provider

[docs](https://docs.aws.amazon.com/eks/latest/userguide/aws-load-balancer-controller.html)

```sh
helm install aws-load-balancer-controller eks/aws-load-balancer-controller \
  -n kube-system \
  --set clusterName=<cluster name> \
  --set serviceAccount.create=false \
  --set serviceAccount.name=aws-load-balancer-controller \
  --set region=eu-central-1 \
  --set vpcId=<newvpcid>
```

## Deploy httpbin to cluster

```sh
kubectl create deployment --image=kennethreitz/httpbin --replicas=3 --port=80
```

## Running k6 test

```sh
k6 run script.js
```
