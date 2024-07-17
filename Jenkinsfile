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
                script {
                    // Instalar Python y Pip si no están instalados
                    sh 'apt update && apt install -y python3 python3-pip'

                    // Instalar dependencias del proyecto
                    sh 'pip3 install -r requirements.txt'

                    // Ejecutar pruebas unitarias con pytest
                    sh 'pytest'
                }
            }
        }
    }
}
