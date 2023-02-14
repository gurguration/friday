pipeline {
    agent any
    stages {
        stage('Build and Push Docker Image') {
            when {
                anyOf {
                    branch 'master'
                    tag '1.0.0'
                }
            }
            steps {
                script {
                    def dockerTag = env.BRANCH_NAME == 'master' ? 'master' : env.GIT_TAG_NAME == '1.0.0' ? '1.0.0' : null

                    if (dockerTag) {
                        docker.build("mydockerhubuser/myimage:${dockerTag}").push()
                    } else {
                        error("Invalid tag: ${env.GIT_TAG_NAME}")
                    }
                }
            }
        }
    }
    post {
        success {
            sh 'poetry run pre-commit run --all-files'
        }
    }
}
