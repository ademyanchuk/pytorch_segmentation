import random, string
from colab_ssh import launch_ssh
import getpass

def ssh_to_colab():
    password = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(20))

    #Ask token
    print("Copy authtoken from https://dashboard.ngrok.com/auth")

    authtoken = getpass.getpass()

    #Create tunnel
    launch_ssh(authtoken, password)
    #Print root password
    print("Root password: {}".format(password))
