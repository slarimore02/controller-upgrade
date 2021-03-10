# Ansible Playbook for Automating Controller Upgrades

## Summary
This playbook and collection of roles allow an administrator to specify either a controller base image or patch to upgrade. It will determine whether the image requires an upload to the controller, and will upload if necessary. From there, it will determine if the image is a patch or system image, then perform the appropriate operation.

Please define variables in the `vars.yml` file before use.


## Regarding Virtual Environments
If you choose to use a Python virtual environment, make sure that you set the ansible_python_interpreter to the appropriate Python binary as shown below.

```
python3 -m venv env
source env/bin/activate
pip3 install -r requirements.txt
ansible-playbook upgrade.yml -u admin -kK --extra-vars="avi_api_version=20.1.4 ansible_python_interpreter=$(which python)"
```