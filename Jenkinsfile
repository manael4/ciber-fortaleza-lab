pipeline {
    agent any

    stages {
        stage('Checkout (Ingredientes)') {
            steps {
                echo 'Descargando la receta de BioGuard...'
                checkout scm
            }
        }

        stage('Build (Cocinar)') {
            steps {
                echo 'Cocinando la imagen Docker...'
                sh 'docker build -t bioguard-app .'
            }
        }

        stage('Test (Control de Calidad)') {
            steps {
                echo 'Auditoría de seguridad con PyBuilder...'
                // MODIFICACIÓN CISO: Cambiamos 'python test.py' por 'pyb'
                sh 'pyb'
            }
        }

        stage('Deploy (Entrega)') {
            steps {
                echo 'Desplegando en Producción Segura...'
                sh 'docker rm -f bioguard-prod || true'
                // MODIFICACIÓN CISO: Puerto cambiado de 5000 a 8443
                sh 'docker run -d --name bioguard-prod -p 8443:5000 bioguard-app'
                echo '¡Servicio BioGuard disponible en http://localhost:8443!'
            }
        }
    }

    post {
        always {
            echo 'Limpiando la cocina...'
            sh 'docker image prune -f'
        }
        success {
            echo '🎉 ¡Pipeline completado con éxito! Calidad 100% asegurada.'
        }
        failure {
            echo '🚑 ¡ALERTA! El pipeline ha fallado. Revisa la cobertura de PyBuilder.'
        }
    }
}
