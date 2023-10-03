
pipeline {
    agent any

    environment {
        PYTHON_VERSION = 'python3'
        DJANGO_SETTINGS_MODULE = 'lakshya.settings'
        DOCKER_IMAGE = 'luhpelayo/ctfbackend:latest'
    }

    stages {
        stage('Checkout') {
            steps {
                //checkout([$class: 'GitSCM', branches: [[name: 'main']], userRemoteConfigs: [[url: 'https://github.com/luhpelayo/lakshya.git']]])
                 echo 'Git Checkout Completed'
            }
        }

        stage('Setup') {
            steps {
                sh "${PYTHON_VERSION} -m pip install Django==4.2"
            }
        }

        stage('Test') {
            steps {
                sh "${PYTHON_VERSION} manage.py test"
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build(DOCKER_IMAGE, '-f Dockerfile .')
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                script {
                    docker.withRegistry('', 'docker-pelayo') {
                        docker.image(DOCKER_IMAGE).push()
                    }
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    // Autenticación en Docker Hub
                    withDockerRegistry([credentialsId: 'docker-pelayo', url: 'https://index.docker.io/v1/']) {
                        // Descargar la imagen desde Docker Hub
                        docker.image(DOCKER_IMAGE).pull()
                        
                        // Ejecutar el contenedor en tu instancia EC2
                        docker.image(DOCKER_IMAGE).withRun('-p 8000:8000') {
                        
                        }
                    }
                }
            }
        }
    }

    post {
        always {
            script {
                docker.image(DOCKER_IMAGE).remove()
            }
        }
    }
}