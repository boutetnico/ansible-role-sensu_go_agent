[![tests](https://github.com/boutetnico/ansible-role-sensu-go-agent/workflows/Test%20ansible%20role/badge.svg)](https://github.com/boutetnico/ansible-role-sensu-go-agent/actions?query=workflow%3A%22Test+ansible+role%22)
[![Ansible Galaxy](https://img.shields.io/badge/galaxy-boutetnico.sensu_go_agent-blue.svg)](https://galaxy.ansible.com/boutetnico/sensu_go_agent)

ansible-role-sensu-go-agent
===========================

This role installs and configures [Sensu Agent](https://docs.sensu.io/sensu-go/latest/reference/agent/).

It is part of a family of Ansible roles allowing to setup and configure Sensu Go components:

- [ansible-role-sensu-go-agent](https://github.com/boutetnico/ansible-role-sensu-go-agent)
- [ansible-role-sensu-go-cli](https://github.com/boutetnico/ansible-role-sensu-go-cli)
- [ansible-role-sensu-go-backend](https://github.com/boutetnico/ansible-role-sensu-go-backend)

Requirements
------------

Ansible 2.7 or newer.

Supported Platforms
-------------------

- [Debian - 10 (Buster)](https://wiki.debian.org/DebianBuster)
- [Debian - 11 (Bullseye)](https://wiki.debian.org/DebianBullseye)
- [Ubuntu - 18.04 (Bionic Beaver)](http://releases.ubuntu.com/18.04/)
- [Ubuntu - 20.04 (Focal Fossa)](http://releases.ubuntu.com/20.04/)

Role Variables
--------------

| Variable                      | Required | Default                       | Choices   | Comments                                       |
|-------------------------------|----------|-------------------------------|-----------|------------------------------------------------|
| sensu_agent_dependencies      | true     | `[apt-transport-https,gnupg]` | list      |                                                |
| sensu_agent_extra_packages    | true     | `[]`                          | list      |                                                |
| sensu_agent_package_state     | true     | `present`                     | string    | Use  `latest` to upgrade.                      |
| sensu_agent_user_extra_groups | true     | `[]`                          | list      | Agent's user secondary groups.                 |
| sensu_agent_config            | true     |                               | dict      | Configuration object, see `defaults/main.yml`. |

Dependencies
------------

None

Example Playbook
----------------

    - hosts: all
      roles:
        - role: ansible-role-sensu-go-agent

Testing
-------

## Debian

    molecule --base-config molecule/shared/base.yml test --scenario-name debian-10
    molecule --base-config molecule/shared/base.yml test --scenario-name debian-11

## Ubuntu

    molecule --base-config molecule/shared/base.yml test --scenario-name ubuntu-1804
    molecule --base-config molecule/shared/base.yml test --scenario-name ubuntu-2004

License
-------

MIT

Author Information
------------------

[@boutetnico](https://github.com/boutetnico)
