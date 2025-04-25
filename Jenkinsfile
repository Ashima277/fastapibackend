pipeline {
    agent any

    environment {
        PROJECT_ID ='python-backend-457816'
        REGION = 'us-central1'
        REPO_NAME = 'python-repo'
        IMAGE = "$REGION-docker.pkg.dev/$PROJECT_ID/$REPO_NAME/fastapi-survey:latest"
        CLUSTER = 'python-cluster'
        CLUSTER_ZONE = 'us-central1-a'
        DEPLOYMENT_NAME = 'python-app'
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/Ashima277/fastapibackend'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $IMAGE .'
            }
        }

        stage('Push Docker Image to Artifact Registry') {
            steps {
                withCredentials([file(credentialsId: 'gsaid', variable: 'GOOGLE_APPLICATION_CREDENTIALS')]) {
                    sh '''
                        gcloud auth activate-service-account --key-file=$GOOGLE_APPLICATION_CREDENTIALS
                        gcloud auth configure-docker $REGION-docker.pkg.dev --quiet
                        docker push $IMAGE
                    '''
                }
            }
        }

        stage('Deploy to GKE') {
            steps {
                withCredentials([file(credentialsId: 'gsaid', variable: 'GOOGLE_APPLICATION_CREDENTIALS')]) {
                    sh '''
                        gcloud auth activate-service-account --key-file=$GOOGLE_APPLICATION_CREDENTIALS
                        gcloud container clusters get-credentials $CLUSTER --zone $CLUSTER_ZONE --project $PROJECT_ID
                        kubectl apply -f k8s/deployment.yaml
                        kubectl apply -f k8s/service.yaml
                    '''
                }
            }
        }
    }
}
