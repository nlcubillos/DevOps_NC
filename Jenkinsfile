pipeline {
    agent any

    stages {
        stage('Clonar repositorio') {
            steps {
                script {
                    def workspaceDir = pwd()  // Obtener el directorio de trabajo del pipeline
                    echo "Directorio de trabajo: ${workspaceDir}"
                    git 'https://github.com/nlcubillos/DevOps_NC.git'
                }
            }
        }

        stage('Ejecutar pruebas unitarias') {
            steps {
                script {
                    def workspaceDir = pwd()  // Obtener nuevamente el directorio de trabajo (si es necesario)
                    sh "ls -la ${workspaceDir}"  // Listar contenido del directorio de trabajo
                    sh 'pytest'  // Ejecutar pruebas unitarias
                }
            }
        }
    }
}
