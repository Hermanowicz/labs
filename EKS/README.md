# EKS Training & Labs

[Go to links:](#links)

---

## Creating cluster using eksctl

```bash
eksctl create cluster --name <my_claster> --region eu-central-1 --with-oidc\
--fargate --full-ecr-access --alb-ingress-access -v --dry-run # remove dry-run after test.
```

## Enabling loging in eks cluster

```bash
eksctl utils update-claster-logging --enable-types=all
```

## Listing available plugins for specified cluster

```bash
eksctl utils describe-addon-versions --cluster <cluster-name>
```

## Adding plugin to cluster

- [ ] creating role for cni form aws cli

```bash
eksctl create addon --name vpc-cni --version 1.7.5 --service-account-role-arn=<role-arn>
```

## Enabling KMS encryption on eks cluster(secrets)

- [ ] creating key in kms from aws cli
  
```bash
$ eksctl utils enable-secrets-encryption --cluster=kms-cluster\
 --key-arn=arn:aws:kms:us-west-2:<account>:key/<key> --region=<region>
```

## Switching from public k8s api access to privet

```bash
eksctl utils update-cluster-endpoints\
 --name=<clustername> --private-access=true --public-access=false
```

> OR limit to specified cidr

```bash
eksctl utils set-public-access-cidrs --cluster=<cluster> 1.1.1.1/32,2.2.2.0/24
```

---

## Links

[EKS Docs](https://docs.aws.amazon.com/eks/latest/userguide/what-is-eks.html) <br/>
[eksctl cli](https://eksctl.io/) <br/>
[EKS Workshop](https://www.eksworkshop.com/) <br/>
[Containers from couch](https://www.youtube.com/containersfromthecouch) <br/>
[Docker Docs](https://docs.docker.com/reference/) <br/>
[Kubernetes CLI Ref / Docs](https://kubernetes.io/docs/reference/kubectl/cheatsheet/) <br/>
