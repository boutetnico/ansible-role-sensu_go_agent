[![tests](https://github.com/boutetnico/ansible-role-sensu_go_agent/workflows/Test%20ansible%20role/badge.svg)](https://github.com/boutetnico/ansible-role-sensu_go_agent/actions?query=workflow%3A%22Test+ansible+role%22)
[![Ansible Galaxy](https://img.shields.io/badge/galaxy-boutetnico.sensu_go_agent-blue.svg)](https://galaxy.ansible.com/boutetnico/sensu_go_agent)

ansible-role-sensu_go_agent
===========================

This role installs and configures [Sensu Agent](https://docs.sensu.io/sensu-go/latest/reference/agent/).

It is part of a family of Ansible roles allowing to setup and configure Sensu Go components:

- [ansible-role-sensu_go_agent](https://github.com/boutetnico/ansible-role-sensu_go_agent)
- [ansible-role-sensu_go_cli](https://github.com/boutetnico/ansible-role-sensu_go_cli)
- [ansible-role-sensu_go_backend](https://github.com/boutetnico/ansible-role-sensu_go_backend)

Requirements
------------

Ansible 2.10 or newer.

Supported Platforms
-------------------

- [Debian - 11 (Bullseye)](https://wiki.debian.org/DebianBullseye)
- [Ubuntu - 22.04 (Jammy Jellyfish)](http://releases.ubuntu.com/22.04/)

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
        - role: ansible-role-sensu_go_agent

Testing
-------

## Debian

    molecule --base-config molecule/shared/base.yml test --scenario-name debian-11

## Ubuntu

    molecule --base-config molecule/shared/base.yml test --scenario-name ubuntu-2204

License
-------

MIT

Author Information
------------------

[@boutetnico](https://github.com/boutetnico)
