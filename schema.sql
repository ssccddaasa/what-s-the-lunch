

#create database lunch;
create table restaurant (
	id int auto_increment primary key not null,
    resName varchar(25) unique not null,
    Email varchar(100) unique not null,
    Password varchar(150) unique not null ,
    location varchar (250) not null ,
    Description varchar(1000),
    image varchar(50) default"default.png",
    phone varchar(25) not null,
    type varchar(25) default "مطعم"
    );

create table user (
	id int auto_increment primary key not null,
    name varchar(25) unique not null,
    Email varchar(100) unique not null,
    Password varchar(150) unique not null ,
    image varchar(50) default"default2.png",
    phone varchar(25) not null,
    location varchar (250) not null 
    );
    
create table meal (
	meal_number int auto_increment primary key not null,
	title varchar(25) not null,
    type varchar(25) default "طبيخ",
    price float not null,
    Description varchar(1000),
    resId int not null,
    image varchar(50) default"default3.png",
    foreign key (resId) references restaurant(id)
    );
    
create table res_user (
	resId int not null,
	id int not null,
	foreign key (resId) references restaurant(id),
    foreign key (id) references user(id),
    constraint pk_res_uesr primary key (resid,id)
    );
    
create table orderr (
    ordnum int primary key auto_increment,
	resId int ,
	id int ,
    meal_number int ,
	foreign key (resId) references restaurant(id) ON DELETE CASCADE,
    foreign key (id) references user(id) ON DELETE CASCADE,
    foreign key (meal_number) references meal(meal_number) ON DELETE CASCADE
    );
    

drop table orderr;
drop table res_user;
drop table meal;
drop table restaurant;
drop table user;

select * 
from orderr;

insert into user
values (1,"saleh","s.lala@gmail.com","1234542134","kl.png","123214","attil");


select m.meal_number, m.title, m.type, m.price, m.Description,m.image,m.resId
from meal m inner join restaurant r
on m.resId = r.id ;
SET SQL_SAFE_UPDATES = 0;
delete from user;
   
 select r.resName, r.id as idd
 from res_user rs inner join restaurant r
 on rs.resId = r.id
 where rs.id = 3
 

