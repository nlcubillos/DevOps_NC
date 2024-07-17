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
                    // Instalar dependencias si es necesario
                    sh 'pip install -r requirements.txt'  // Asegúrate de que esto sea necesario según tu proyecto
                    sh 'pip install pytest'  // Instala pytest si no está instalado

                    // Ejecutar pruebas unitarias con pytest
                    sh 'pytest'
                }
            }
        }
    }
}
