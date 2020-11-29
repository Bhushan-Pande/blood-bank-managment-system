create database blood19;
use blood19;
create table admin1(Admin_id int primary key, username varchar(30), password varchar(30));
drop table Blood_info;
drop table donor1;
drop table Contact_info;
drop table donor3;
drop table admin1;
drop table Request;
drop table feedback;
drop table history1;
drop table availability;
create table Request(Request_id int primary key, Admin_id int, Donor_id int, foreign key (donor_id) references donor(donor_id), foreign key(Admin_id) references admin1(Admin_id));
create table Contact_info(dname varchar(30), Donor_id int, Admin_id int, phoneno varchar(30), address varchar(30), foreign key (Donor_id) references donor1(Donor_id),foreign key(Admin_id) references admin1(Admin_id));
create table Blood_info(dname varchar(30), Donor_id int, Blood_group varchar(10), Admin_id int, foreign key(Donor_id) references donor1(Donor_id));
insert into admin1 values(1200, "Ashish","hello"); 
create table test(test_id int auto_increment primary key,name varchar(30));
insert into test(name) values('kewal');
insert into test(name) values('adi');
select * from test;
select * from donor;
select * from admin1;
create table donor1(Donor_id int primary key auto_increment, Admin_id int, dname varchar(30), bloodgroup varchar(10),gender varchar(30), address varchar(30), phoneno varchar(30),foreign key(admin_id) references admin1(admin_id));
select * from donor1;
create table donor2(Donor_id int primary key auto_increment,dname varchar(30), bloodgroup varchar(10),gender varchar(30), address varchar(30), phoneno varchar(30));
select * from donor2;
create table donor3(d_id int primary key auto_increment, doname varchar(30), bgp varchar(30), Gen varchar(30), adr varchar(30),pno varchar(30));
select * from donor3;
select * from Blood_info;
UPDATE donor1 set bloodgroup='B' where Donor_id=1;
alter table Blood_info drop primary key;
drop table Blood_info;
create table Blood_info(dname varchar(30), Donor_id int, Blood_group varchar(10), Admin_id int, foreign key(Donor_id) references donor1(Donor_id));
UPDATE donor1 set bloodgroup='B' where Donor_id=1;
create table Contact_info(dname varchar(30), Donor_id int, Admin_id int, phoneno varchar(30), address varchar(30), foreign key (Donor_id) references donor1(Donor_id),foreign key(Admin_id) references admin1(Admin_id));
select * from Contact_info;
create table feedback(feedback_id int primary key auto_increment, dname varchar(30),feedback_data varchar(100));
select * from feedback;
create table history1(Donor_id int, dname varchar(30),date1 date,foreign key (Donor_id) references donor1(Donor_id));
drop table history1;
create table history1(Donor_id int, dname varchar(30),date1 datetime default now(),foreign key (Donor_id) references donor1(Donor_id));
drop table history1;
select * from history1;
delimiter $$
drop trigger if exists available;
create trigger available after insert on history1 for each row
begin
declare city1 varchar(30);
declare Blood_group varchar(30);
declare c int;
SELECT 
  address,bloodgroup
INTO 
    city1,blood_group
FROM 
    donor1
WHERE 
    donor_id=new.donor_id;
select count(quantity) into c from availability where city=city1; 
if c=0 then 
insert into availability values(city1,blood_group,1);
else
update availability set quantity=quantity+1 where blood_group=blood_group and city=city1;
end if;
end$$
delimiter ;
drop trigger update_history;

create table address1(city varchar(30), Blood_group varchar(10),no_of_donors int default 0);
delimiter $$
create trigger adrr after insert on donor1 for each row
begin
end $$
delimiter ;
create table availability(city varchar(30),Blood_group varchar(30), quantity int);
select * from donor1;
insert into availability values('Amravati','A',2);
select * from availability;
truncate availability;
drop table availability;
SELECT count(quantity) FROM availability where city='Amravati';
show triggers from blood19;
SET SQL_SAFE_UPDATES = 0;
insert into history1(Donor_id,dname)values(2,'Kavisha');
truncate history1;




