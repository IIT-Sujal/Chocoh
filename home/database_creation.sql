create database sujal24$chocoh;
use sujal24$chocoh;
create table user(user_id int primary key not null auto_increment,name char(50) not null,password char(50) not null,email_id char(50),contact_no char(10),user_wallet int default '0');
create table orders(order_id int primary key not null auto_increment,total_amount int,delivery_address char(100),mobile_no char(10),delivery_date date,order_date date,delivery_status char(20) default 'not started',return_status char(10) default 'false',order_status char(10) default 'not paid');
create table chocolate(chocolate_id int primary key not null auto_increment,price int,name char(50) not null,quantities_available int,quantities_sold int,description char(200) default 'Wonderful Product',ratings int);
create table bank_details(card_no char(16) primary key not null,bank_name char(50),card_type char(50),data_on_card char(50));
create table feedback(feedback_id int primary key not null auto_increment,user_id int, foreign key(user_id) references user(user_id), chocolate_id int, foreign key(chocolate_id) references chocolate(chocolate_id),approval boolean,upvotes int,content char(200));
create table payment(payment_id int primary key not null auto_increment,status char(10));
create table shipper(shipper_id int primary key not null auto_increment,delivery_charges int,location char(50));
create table buys(chocolate_id int, foreign key(chocolate_id) references chocolate(chocolate_id),user_id int, foreign key(user_id) references user(user_id));
create table purchased_product(order_id int, foreign key(order_id) references orders(order_id), chocolate_id int, foreign key(chocolate_id) references chocolate(chocolate_id),quantity int);
create table user_cart(user_id int, foreign key(user_id) references user(user_id),chocolate_id int, foreign key(chocolate_id) references chocolate(chocolate_id),quantity int default '1');
create table contact_info(user_id int, foreign key(user_id) references user(user_id),contact_no char(10));
create table place_order(user_id int, foreign key(user_id) references user(user_id),order_id int, foreign key(order_id) references orders(order_id));
create table shipper_info(shipper_id int, foreign key(shipper_id) references shipper(shipper_id), contact_no char(10));
create table transaction(order_id int, foreign key(order_id) references orders(order_id),payment_id int, foreign key(payment_id) references payment(payment_id),time_stamp time);
create table delivered_by(order_id int, foreign key(order_id) references orders(order_id),shipper_id int,foreign key(shipper_id) references shipper(shipper_id));
create table pays(user_id int ,foreign key(user_id) references user(user_id),payment_id int, foreign key(payment_id) references payment(payment_id));
create table ceo(ceo_id int primary key auto_increment,email_id char(50), password char(50));
create table messages(message_id int auto_increment primary key,name char(50),email_id char(50),contact_no char(20),messages text);

insert into chocolate(name,price,quantities_available,quantities_sold,ratings) values("fruit and nut1",300,10,10,5);
insert into chocolate(name,price,quantities_available,quantities_sold,ratings) values("fruit and nut2",301,10,10,5);
insert into chocolate(name,price,quantities_available,quantities_sold,ratings) values("fruit and nut3",302,10,10,5);
insert into chocolate(name,price,quantities_available,quantities_sold,ratings) values("fruit and nut4",303,10,10,5);
insert into chocolate(name,price,quantities_available,quantities_sold,ratings) values("fruit and nut5",304,10,10,5);
insert into chocolate(name,price,quantities_available,quantities_sold,ratings) values("fruit and nut6",305,10,10,5);
INSERT INTO user(name,password,email_id,contact_no) values("sujal","s","s@s","9");
INSERT INTO ceo(email_id,password) values("k@k","k");