# Cloud Native Platform Engineering Lab

A hands-on lab for building, deploying, operating, and troubleshooting a small cloud-native application platform.

I’m building this incrementally so each stage is understood and tested before moving on to the next one.

## Where am I right now 

The first version of the application is running locally with FastAPI.

Current endpoints:

- `/` - basic application response
- `/healthz` - application health check
- `/version` - current application version

Basic API tests are also in place and can be run locally with `pytest`.

## What is next :

Right now the focus is on getting the application and testing workflow right before moving into containerization.

The next steps are:

- containerize the application
- deploy it to Kubernetes
- package it with Helm
- add CI with GitHub Actions
- add deployment validation and smoke tests
- build controlled troubleshooting scenarios

Later stages will introduce infrastructure as code, AWS, EKS, GitOps, observability, and OpenShift where they make sense.

## Why This Project :

The goal is not just to get workloads running.

I want to understand how the platform behaves, how to validate changes, what breaks during deployments, how to troubleshoot failures, and how to improve the delivery workflow over time.

## Status

✅ GitHub repository setup complete  
✅ Initial FastAPI application running locally  
✅ Basic API tests passing  
🚧 Containerization next  
📋 Kubernetes, Helm, CI/CD and cloud stages planned