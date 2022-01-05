# sets up a client SSH configuration file so that we can connect to a server without using a password

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
