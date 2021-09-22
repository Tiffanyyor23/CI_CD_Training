pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/Tiffanyyor23/CI_CD_Training'
            }
        }
        stage('Unit Test') {
            sh "python3 ./test_calculatorController.py"
        }
    }
}
