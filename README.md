# Cloud Native Platform Engineering Lab

A hands-on lab for building, deploying, operating, and troubleshooting a small cloud-native application platform.

I’m building this incrementally so each stage is understood and tested before moving on to the next one.

## Current Progress

The first FastAPI application is running locally with:

- `/` - basic response
- `/healthz` - health check
- `/version` - application version

Basic API tests are in place with `pytest`.

The application has also been containerized with Docker and tested with host-to-container port mapping.

## What's Next?

Next milestones:

- Kubernetes deployment
- Kubernetes Service and health probes
- resource requests and limits
- Helm
- GitHub Actions CI
- deployment validation and smoke tests
- troubleshooting scenarios

Later stages will include Terraform, AWS, EKS, GitOps, observability, and OpenShift where they make sense.

## Status

✅ GitHub setup complete  
✅ FastAPI application running  
✅ Basic API tests passing  
✅ Docker containerization complete  
🚧 Kubernetes next  
📋 Helm, CI/CD and cloud stages planned