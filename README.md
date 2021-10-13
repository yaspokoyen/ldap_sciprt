# LDAP-Script
[python]

Docker hub
https://hub.docker.com/r/yaspokoyen/ldap_alpine

docker pull yaspokoyen/ldap_alpine:v1

Docker run command:

docker run --rm -e LOGIN=your_server -e PASS=your_password -e SERVER=your_server yaspokoyen/ldap_alpine:v1
