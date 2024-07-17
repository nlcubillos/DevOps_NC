pipeline {
    agent any

    stages {
        stage('Clonar repositorio') {
            steps {
                git 'https://github.com/nlcubillos/DevOps_NC.git'
            }
        }

        stage('Ejecutar pruebas unitarias') {
            steps {
                // Aquí deberías incluir los comandos para ejecutar tus pruebas unitarias
                // Por ejemplo, para Python con pytest:
                sh 'pytest'
            }
        }

        stage('Análisis de calidad del código') {
            steps {
                // Aquí deberías incluir los comandos para ejecutar SonarQube o SonarCloud
                // Por ejemplo, analizando un proyecto de Python con SonarQube Scanner
                withSonarQubeEnv('SonarQube_Server') {
                    sh 'sonar-scanner'
                }
            }
        }

        stage('Construir imagen Docker y subir a Docker Hub') {
            steps {
                // Construir imagen Docker
                sh 'docker build -t nombre_usuario/nombre_imagen .'
                // Subir imagen a Docker Hub (requiere login previo)
                withCredentials([usernamePassword(credentialsId: 'dockerhub', usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
                    sh 'docker login -u $DOCKER_USERNAME -p $DOCKER_PASSWORD'
                    sh 'docker push nombre_usuario/nombre_imagen'
                }
            }
        }
    }
}
