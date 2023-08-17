# UltimateCICDPipeline
This is a Ultimate CICD Pipeline implementation using, Jenkins, ArgoCD and Kubernetes.
This end-to-end Jenkins pipeline will automate the entire CI/CD process for a Django application, from code checkout to production deployment.


Today I build a ultimate end-to-end CI/CD pipeline that automates the entire CI/CD process for a Django application.

It works with the following flow: Developer pushes the code to GitHub repo. GitHub webhooks then triggers the jenkis build and if the build is successful the docker image is pushed to dockerhub and manifest repo is updated. ArgoCD continuesly monitors the manifest repo and deploys the docker image to Kubernetes cluster.


. 



