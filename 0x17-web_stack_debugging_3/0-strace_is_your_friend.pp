# fixing typing error at server configfile
exec { 'replace':
  command => 'sudo sed -ie 's/class-wp-locale.phpp/class-wp-locale.php/' /var/www/html/wp-settings.php'
}

exec { 'restart':
  command => 'sudo cat /var/www/html/wp-settings.php | grep class-wp-locale.php'
}
