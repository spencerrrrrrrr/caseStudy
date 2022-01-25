pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'docker build -t spencerhurrle/case-study:latest .'
            }
        }
        stage('Docker Push') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhublogin', passwordVariable: 'dockerHubPassword', usernameVariable: 'dockerHubUser')]) {
                    sh "docker login -u ${env.dockerHubUser} -p ${env.dockerHubPassword}"
                    sh 'docker push spencerhurrle/case-study:latest'
                }
            }
        }
    }
}
