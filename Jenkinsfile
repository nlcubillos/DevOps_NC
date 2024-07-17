pipeline {
    agent any

    stages {
        stage('Clonar Repositorio') {
            steps {
                git 'git@github.com:nlcubillos/DevOps_NC.git'
            }
        }

        stage('Ejecutar Pruebas Unitarias') {
            steps {
                sh 'pytest --junitxml=report.xml'
                junit 'report.xml'
            }
        }

        // Otras etapas del pipeline se pueden agregar aquí
    }

    // Opcionalmente, puedes agregar post-actions para manejar acciones después de las etapas
    post {
        always {
            // Puedes agregar acciones que se ejecuten siempre, como limpiar recursos temporales
        }
    }
}
