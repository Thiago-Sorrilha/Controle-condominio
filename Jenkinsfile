pipeline {
    agent any
    
    stages {
        stage('Checkout & Info') {
            steps {
                echo 'A preparar o ambiente...'
                sh 'uname -a'
                sh 'whoami'
                sh 'pwd'
            }
        }
        stage('Build & Test simulado') {
            steps {
                echo 'A executar compilação e testes...'
                sh 'echo "Código compilado com sucesso!"'
            }
        }
        stage('Deploy') {
            steps {
                echo 'A realizar deploy simulado para ambiente de teste...'
            }
        }
    }
    
    post {
        success {
            echo 'Pipeline executada com sucesso!'
        }
        failure {
            echo 'A pipeline falhou!'
        }
    }
}