// node {
//     stage("Hello") {
//         echo "Hello World"
//         https://github.com/Supawich2307/rest_api_test.git
//     }
//     stage("Build") {
//         sh """
//         pwd
//         ls -l
//         python3 app.py
//         """
//     }
//     stage("Build") {
//         def dockerHome = tool 'bookk'
//         env.PATH = "${dockerHome}/bin:${env.PATH}"
//         sh """
//         ls -l
//         cd ~/desktop/restapi2
//         pwd
//         source venv/bin/activate
//         """
//     }
//     stage("Run"){
//         sh """
//         cd ~/desktop/restapi2/rest
//         python3 app.py
//         """
//     }
// }
node{
    stage("SCM") {
        git branch: "main", url: "https://github.com/bookPNG/restapi.git"
    }
    stage('Initialize'){
        def dockerHome = tool 'bookk'
        env.PATH = "${dockerHome}/bin:${env.PATH}"
        sh "echo ${env.PATH}"
    }
    stage("Build") {
      sh "pwd"
      sh "docker build ."
    }
}