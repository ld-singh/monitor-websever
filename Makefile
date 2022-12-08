#######################################
#
# Makefile for monitor_webserver.py
#
# ####################################



## Install dependencies
install-requirements:
        pip3 install boto3



## Run the monitoring script
monitor: install-requirements
        python3 monitor_webserver.py
