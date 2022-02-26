It is possible to use Jupyterlab on your rpi from your main PC.

The description is taken from there: https://medium.com/analytics-vidhya/jupyter-lab-on-raspberry-pi-22876591b227

Mainly:

First run the following commands:

$ sudo apt-get update

$ sudo apt-get install python3-pip

$ sudo pip3 install setuptools

$ sudo apt install libffi-dev

$ sudo pip3 install cffi

Then you install Jupyterlab;

$ pip3 install jupyterlab

And you create a new directory for your notebooks:

$ mkdir notebooks

$ jupyter lab --notebook-dir=~/notebooks


You can then install Jupyterlab as a service on the rpi. For this you need to create the
/etc/systemd/system/jupyter.service file.

A priori, the jupyterlab command is located here:

/home/pi/.local/bin/jupyter-lab

Else you have to adapt.

In the jupyter.service, put the following:

[Unit]

Description=Jupyter Lab

[Service]

Type=simple

PIDFile=/run/jupyter.pid

ExecStart=/bin/bash -c "/home/pi/.local/bin/jupyter-lab --ip="0.0.0.0" --no-browser --notebook-dir=/home/pi/notebooks"

User=pi

Group=pi

WorkingDirectory=/home/pi/notebooks

Restart=always

RestartSec=10

[Install]

WantedBy=multi-user.target

And enable the service:

$ sudo systemctl enable jupyter.service

You may reboot, then go to: http://<rpi ip address>:8888
  
 You have to enter the token than you can retrieve by:
  
 $ sudo systemctl status jupyter.service
  
 
  
  
  
  
  

$ sudo systemctl daemon-reload

