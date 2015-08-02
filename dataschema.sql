drop table if exists users;
create table users (
  id integer primary key ,
  name string not null,
  email string not null
);
