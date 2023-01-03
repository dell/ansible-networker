# DellEMC NetWorker Ansible Collection

Ansible collection is used to get, create, modify or delete the networker resources to automate the configuration tasks easy and fast.



**Pre-requisites**
 - Python V3.8 or higher

**Installation of Ansible Collection**
  
  Use below command to install the collection.
  
  `ansible-galaxy collection install git+https://github.com/dell/ansible-networker.git`
  
  Install all packages from the requirements.txt file
  
  `pip install <collection-install-path>/dellemc/networker/requirements.txt`

**Inventory file**

  Build the inventory file as below
  ```
  [nve]
  10.0.0.6

  [nve:vars]
  ansible_port = 22
  ansible_user = root
  private_key_file = /home/admin/.ssh/id_rsa

  nsr_port = 9090
  nsr_user = 'administrator' # NMC User name
  nsr_pass = 'p@ssw0d123' # NMC User Password. Use the 
```
**Ansible Playbook**

  To make the rest api call from the host you are running the playbook; use below parameter at the top of the playbook
  
  `connection: local`
  
**Sample Playbook**

```
- name: Get the volume information.
  hosts: all
  connection: local
  gather_facts: false
  tasks:
    - name: Get volume information by volume name
      dellemc.networker.volumes:
        state: get
        query_params:
          name: VOLNAME.01
      register: volinfo

    - debug:
        msg: "{{ volinfo }}"
  ```
  
  #Copyright ©️ 2022 Dell Inc. or its subsidiaries.
