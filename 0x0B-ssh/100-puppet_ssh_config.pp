# sets up a client SSH configuration file so that we can connect to a server without using a password

file_line { 'Declare identity file':
  path    => '~/.ssh/config',
  line    => '    IdentityFile ~/.ssh/holberton',
  replace => true,
}

file_line { 'Turn off passwd authentication':
  path    => '~/.ssh/config',
  line    => '    PasswordAuthentication no',
  replace => true,
}
