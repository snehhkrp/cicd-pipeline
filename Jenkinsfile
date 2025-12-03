// pipeline {
//     agent any

//     environment {
//         IMAGE_NAME = "cicd-pipeline-image"
//         CONTAINER_NAME = "cicd-pipeline-container"
//     }

//     stages {
//         stage('Checkout') {
//             steps {
//                 echo "Source code checked out"
//             }
//         }

//         stage('Build Docker Image') {
//             steps {
//                 bat "docker build -t %IMAGE_NAME% ."
//             }
//         }

//         stage('Deploy Container') {
//             steps {
//                 bat """
//                 docker stop %CONTAINER_NAME% || exit 0
//                 docker rm %CONTAINER_NAME% || exit 0
//                 docker run -d -p 5000:5000 --name %CONTAINER_NAME% %IMAGE_NAME%
//                 """
//             }
//         }
//     }

//     post {
//         success {
//             echo "✅ UI deployed successfully via CI/CD"
//         }
//         failure {
//             echo "❌ Pipeline failed"
//         }
//     }
// }


//----------------------------- Revised Jenkinsfile -----------------------------
// pipeline {
//     agent any

//     environment {
//         IMAGE_NAME = "cicd-pipeline-image"
//         CONTAINER_NAME = "cicd-pipeline-container"
//         VERSION = "${BUILD_NUMBER}"
//     }

//     stages {
//         stage('Checkout') {
//             steps {
//                 echo "Source code checked out"
//             }
//         }

//         stage('Build Docker Image') {
//             steps {
//                 bat """
//                 docker build -t %IMAGE_NAME%:%VERSION% -t %IMAGE_NAME%:latest .
//                 """
//             }
//         }

//         stage('Deploy Container') {
//             steps {
//                 bat """
//                 docker stop %CONTAINER_NAME% 2>nul
//                 docker rm %CONTAINER_NAME% 2>nul
//                 docker run -d -p 5000:5000 --name %CONTAINER_NAME% %IMAGE_NAME%:%VERSION%
//                 """
//             }
//         }

//         stage('Health Check') {
//             steps {
//                 bat """
//                  timeout /t 5 /nobreak
//                  curl -f http://localhost:5000 || exit 1
//                 """
//     }
// }

//     }

//     post {
//         success {
//             echo "✅ Deployed Build Version: %VERSION%"
//         }
//     }
// }


//============================= Revised Jenkinsfile with Tests =========================

// pipeline {
//     agent any

//     environment {
//         IMAGE_NAME     = "cicd-pipeline-image"
//         CONTAINER_NAME = "cicd-pipeline-container"
//         VERSION        = "${BUILD_NUMBER}"
//         PORT           = "5000"
//     }

//     stages {
//         stage('Checkout') {
//             steps {
//                 echo "Source code checked out"
//                 // Jenkins has already done the git checkout at this point
//             }
//         }

//         stage('Install Dependencies') {
//             steps {
//                 bat """
//                 python -m pip install --upgrade pip
//                 python -m pip install -r requirements.txt
//                 """
//             }
//         }

//         stage('Lint') {
//             steps {
//                 bat "flake8 ."
//             }
//         }

//         stage('Run Tests') {
//             steps {
//                 bat """
//                     set PYTHONPATH=%CD%
//                      pytest
//                     """
//                 }
// }


//         stage('Build Docker Image') {
//             steps {
//                 bat """
//                 docker build -t %IMAGE_NAME%:%VERSION% -t %IMAGE_NAME%:latest .
//                 """
//             }
//         }

//         stage('Deploy Container') {
//             steps {
//                 bat """
//                 docker stop %CONTAINER_NAME% 2>nul
//                 docker rm %CONTAINER_NAME% 2>nul
//                 docker run -d ^
//                     -e BUILD_VERSION=%VERSION% ^
//                     -p %PORT%:%PORT% ^
//                     --name %CONTAINER_NAME% ^
//                     %IMAGE_NAME%:%VERSION%
//                 """
//             }
//         }

//         stage('Health Check') {
//             steps {
//                 bat """
//                 timeout /t 5 /nobreak
//                 curl -f http://localhost:%PORT%/health || exit 1
//                 """
//             }
//         }
//     }

//     post {
//         success {
//             echo "✅ Pipeline SUCCESS. Deployed Build Version: %VERSION%"
//         }
//         failure {
//             echo "❌ Pipeline FAILED. Check logs above."
//         }
//     }
// }


//============================= Revised Jenkinsfile with Tests =========================

pipeline {
    agent any

    environment {
        BUILD_VERSION = "${env.BUILD_NUMBER}"
        DOCKER_ENV = "true"
    }

    stages {

        stage('Checkout') {
            steps {
                echo "Checking out source code..."
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                bat """
                python -m pip install --upgrade pip
                python -m pip install -r requirements.txt
                """
            }
        }

        stage('Lint') {
            steps {
                bat "flake8 ."
            }
        }

        stage('Run Tests') {
            steps {
                bat "pytest"
            }
        }

        stage('Build Docker Image') {
            steps {
                bat "docker build -t cicd-app-image ."
            }
        }

        stage('Deploy Container') {
            steps {
                bat """
                docker stop cicd-app-container 2>nul || exit 0
                docker rm cicd-app-container 2>nul || exit 0

                docker run -d -p 5000:5000 ^
                    -e BUILD_VERSION=${BUILD_VERSION} ^
                    -e DOCKER_ENV=true ^
                    --name cicd-app-container cicd-app-image
                """
            }
        }

        stage('Health Check') {
            steps {
                script {
                    sleep 5
                    def response = powershell(script: "(Invoke-WebRequest -Uri http://localhost:5000/health).Content", returnStdout: true)
                    echo "Health response: ${response}"
                }
            }
        }
    }

    post {
        success {
            echo "✅ Deployment successful!"
        }
        failure {
            echo "❌ Pipeline failed — check logs!"
        }
    }
}
