include ::ssh

Ssh::Config_entry {
  ensure => present,
  path   => '~/.ssh/config'
}

ssh::config_entry { 'identityfile with no passwd':
  host  => '*',
  lines => [
    '    PasswordAuthentication no',
    '    IdentityFile ~/.ssh/school'
  ]
}
