# increasing maximum mumber of open files in one user
exec { 'change hard limit':
  command => '/bin/sed -ie \'s/holberton hard nofile 5/holberton hard nofile 65535/\' /etc/security/limits.conf'
}

exec { 'change soft limit':
  command => '/bin/sed -ie \'s/holberton soft nofile 4/holberton soft nofile 65535/\' /etc/security/limits.conf'
}
