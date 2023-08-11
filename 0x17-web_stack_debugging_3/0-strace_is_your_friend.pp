# fix errors and automate

exec {'fix_phpp_errors':
  command => "sed -i 's/phpp/php/g' /var/www/html/wp-settings.php",
  path    => '/bin',
}
