# UltimateCICDPipeline
This is a Ultimate CICD Pipeline implementation using, Jenkins, ArgoCD and Kubernetes.
This end-to-end Jenkins pipeline will automate the entire CI/CD process for a Django application, from code checkout to production deployment.


Today I build a ultimate end-to-end CI/CD pipeline that automates the entire CI/CD process for a Django application.

It works with the following flow: Developer pushes the code to GitHub repo. GitHub webhooks then triggers the jenkis build and if the build is successful, the docker image is pushed to dockerhub and manifest repo is updated. ArgoCD continuesly monitors the manifest repo and deploys the docker image to Kubernetes cluster.


. 
Pipeline components:

1. Github is used for source code management of django application, and it also holds the manifest repo for Kubernetes.

2. Jenkins is used as a CI tool, and it is deoployed on a AWS EC2 instance. GitHub webhooks is used for triggering the jenins pipeline. GitHub webhooks triggers the jenkins pipeline on each code push. Jenkins then builds the django application, contenerizes it and pushes the final docker image to dockerhub and it also updates the manifest repo with appropriate image tag. I used docker container as a build agent in Jenkins, it helps in better resource optimization and lowers the overall project cost.

3. Argo CD is a Kubernetes-native continuous deployment (CD) tool. It pulls updated manifast code from Git repository and deploy it directly to Kubernetes cluster. Argo CD continuously monitors the running infrastructure (the actual state) and compare it to declaratively-defined code (the desired state or target state) of the application manifest repo to determine whether they are out of sync, which helps to remediate configuration drift.

4. Kubernetes cluster is configured using miniqube on local machine. Argo CD deploys the contenerized django application on this cluster. 


