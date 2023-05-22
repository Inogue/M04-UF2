  1 create database if not exists EvilCorp;
  2 drop table if exists `users`;
  3 create table `users`(id_user BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY     KEY, username VARCHAR(32) NOT NULL, name VARCHAR(64) NOT NULL, surname VARC    HAR(64), birthday DATE NOT NULL, email VARCHAR(32) NOT NULL, phone VARCHAR(1    5) NOT NULL, country VARCHAR(64) NOT NULL, direction VARCHAR(64), password V    ARCHAR(32), date DATETIME NOT NULL DEFAULT now());
  4 insert into `users`(username, name, surname, birthday, email, phone, country    , direction, password) values ("root", "Hilon", "Musgo", "1971-06-28", "hilo    nmusgo@gmail.com","27666666666","South Africa","EvilCorp666","e1e71757deb074    60abff6678e3cd468f");
  5 create user 'editor'@'localhost' identified by 'enti';
  6 create user 'reader'@'localhost' identified by 'enti';
  7 grant insert, update on EvilCorp.* to 'editor'@'localhost';
  8 grant select on EvilCorp.* to 'reader'@'localhost';
  9 flush privileges;
