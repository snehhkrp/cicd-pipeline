pipeline {
    agent any

    environment {
        IMAGE_NAME = "cicd-pipeline-image"
        CONTAINER_NAME = "cicd-pipeline-container"
    }

    stages {
        stage('Checkout') {
            steps {
                echo "Source code checked out"
            }
        }

        stage('Build Docker Image') {
            steps {
                bat "docker build -t %IMAGE_NAME% ."
            }
        }

        stage('Deploy Container') {
            steps {
                bat """
                docker stop %CONTAINER_NAME% || exit 0
                docker rm %CONTAINER_NAME% || exit 0
                docker run -d -p 5000:5000 --name %CONTAINER_NAME% %IMAGE_NAME%
                """
            }
        }
    }

    post {
        success {
            echo "✅ UI deployed successfully via CI/CD"
        }
        failure {
            echo "❌ Pipeline failed"
        }
    }
}
