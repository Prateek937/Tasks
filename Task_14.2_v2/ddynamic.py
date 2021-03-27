#!/bin/python3
import docker
import json
def get_hosts():
    # Setting the client for Docker
    client = docker.DockerClient()
    # listing all the containers
    containers = client.containers.list()
    ip_add = []
    for cont in containers:
        # getting the IP Addresses of all containers
        container = client.containers.get(cont.short_id)
        ip_add.append(container.attrs['NetworkSettings']['IPAddress'])
    return ip_add

def main():
    # funtion for getting IPs of containers
    ip_add = get_hosts()
    # inventory format
    docker={
            'docker': {
                'hosts': ip_add,
                'vars': {
                    'ansible_connection': 'ssh',
                    'ansible_user': 'root',
                    'ansible_ssh_pass': 'redhat'
                }
            }
    }
    #converting into json
    print(json.dumps(docker))

if __name__ == "__main__":
    main()
