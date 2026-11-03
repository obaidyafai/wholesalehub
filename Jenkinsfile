pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out WholesaleHub source code'
            }
        }

        stage('Inspect Project') {
            steps {
                sh 'pwd'
                sh 'ls -la'
                sh 'ls -la templates'
                sh 'ls -la static'
            }
        }

        stage('Check Python') {
            steps {
                sh 'python3 --version'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'python3 -m venv venv'
                sh 'venv/bin/pip install -r requirements.txt'
            }
        }

        stage('Build Complete') {
            steps {
                echo 'WholesaleHub pipeline completed!'
            }
        }
    }
}

