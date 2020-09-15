import pytest

import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize('name', [
  ('sensu-go-agent'),
])
def test_packages_are_installed(host, name):
    package = host.package(name)
    assert package.is_installed


@pytest.mark.parametrize('name', [
  ('sysstat'),
])
def test_extra_packages_are_installed(host, name):
    package = host.package(name)
    assert package.is_installed

@pytest.mark.parametrize('name', [
  ('adm'),
])
def test_user_belongs_to_its_additional_groups(host, name):
    user = host.user('sensu')
    assert user.contains(name)


@pytest.mark.parametrize('file,user,group,mode,content', [
  ('/etc/sensu/agent.yml', 'root', 'root', 0o644, 'backend-url'),
])
def test_agent_config_file_exist(host, file, user, group, mode, content):
    config = host.file(file)
    assert config.exists
    assert config.is_file
    assert config.user == user
    assert config.group == group
    assert config.mode == mode
    assert config.contains(content)
