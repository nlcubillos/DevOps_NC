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
                    // Instalar pip si no está instalado (solo si es necesario)
                    sh 'apt-get update && apt-get install -y python3-pip'

                    // Instalar pytest y otras dependencias
                    sh 'pip3 install -r requirements.txt'  // Asegúrate de que esto sea necesario según tu proyecto
                    sh 'pip3 install pytest'

                    // Ejecutar pruebas unitarias con pytest
                    sh 'pytest'
                }
            }
        }
    }
}
