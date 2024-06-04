pipeline {
    agent any

    environment {
        PYTHON_ENV = 'env'
    }

    stages {
        stage('Checkout') {
            steps {
                
                git ' https://github.com/Pavansai01/ml-jenkins-pipeline.git'
            }
        }
        stage('Setup') {
            steps {
                sh '''
                    python3 -m venv $PYTHON_ENV
                    source $PYTHON_ENV/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }
        stage('Train Model') {
            steps {
                sh '''
                    source $PYTHON_ENV/bin/activate
                    python train_model.py
                '''
            }
        }
        stage('Test Model') {
            steps {
              
                sh '''
                    source $PYTHON_ENV/bin/activate
                    python test_model.py
                '''
            }
        }
        stage('Deploy Model') {
            steps {
                
                sh '''
                    echo "Model deployment steps go here."
                '''
            }
        }
    }
    post {
        always {
            
            sh 'rm -rf $PYTHON_ENV'
        }
    }
}
