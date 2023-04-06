# Setup the web servers for the deployment of web_static
class nginx_web_static {
  package { 'nginx':
    ensure => 'installed',
  }

  file { '/data/web_static/releases/test/':
    ensure  => 'directory',
    owner   => 'ubuntu',
    group   => 'ubuntu',
    mode    => '0755',
    recurse => true,
  }

  file { '/data/web_static/shared/':
    ensure  => 'directory',
    owner   => 'ubuntu',
    group   => 'ubuntu',
    mode    => '0755',
    recurse => true,
  }

  file { '/data/web_static/releases/test/index.html':
    ensure  => 'file',
    content => '<!DOCTYPE html>
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>',
    owner   => 'ubuntu',
    group   => 'ubuntu',
    mode    => '0644',
  }

  file { '/data/web_static/current':
    ensure  => 'link',
    target  => '/data/web_static/releases/test/',
    owner   => 'ubuntu',
    group   => 'ubuntu',
  }

  file { '/etc/nginx/sites-enabled/default':
    ensure  => 'file',
    owner   => 'root',
    group   => 'root',
    content => "server {
    listen 80 default_server;
    listen [::]:80 default_server;

    root /var/www/html;

    index index.html index.htm index.nginx-debian.html;

    server_name _;

    location / {
        try_files $uri $uri/ =404;
    }

    location /hbnb_static/ {
        alias /data/web_static/current/;
    }
}
",
  }

  service { 'nginx':
    ensure => 'running',
    enable => true,
    require => Package['nginx'],
    subscribe => File['/etc/nginx/sites-enabled/default'],
  }
}

class { 'nginx_web_static': }
