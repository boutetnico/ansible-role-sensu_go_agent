ansible-role-sensu-go-agent
===========================

This role installs and configures [Sensu Agent](https://docs.sensu.io/sensu-go/latest/reference/agent/).

It is part of a family of Ansible roles allowing to setup and configure Sensu Go components:

- [ansible-role-sensu-go-agent](https://github.com/boutetnico/ansible-role-sensu-go-agent)
- [ansible-role-sensu-go-cli](https://github.com/boutetnico/ansible-role-sensu-go-cli)
- [ansible-role-sensu-go-backend](https://github.com/boutetnico/ansible-role-sensu-go-backend)

Requirements
------------

Ansible 2.6 or newer.

Supported Platforms
-------------------

- [Debian - 9 (Stretch)](https://wiki.debian.org/DebianStretch)
- [Debian - 10 (Buster)](https://wiki.debian.org/DebianBuster)
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

    molecule --base-config molecule/shared/base.yml test --scenario-name debian-9
    molecule --base-config molecule/shared/base.yml test --scenario-name debian-10

## Ubuntu

    molecule --base-config molecule/shared/base.yml test --scenario-name ubuntu-1804
    molecule --base-config molecule/shared/base.yml test --scenario-name ubuntu-2004

License
-------

MIT

Author Information
------------------

[@boutetnico](https://github.com/boutetnico)
