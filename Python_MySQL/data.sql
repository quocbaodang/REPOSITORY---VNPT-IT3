create database student
go

use student 
go

create table Info
(
	name nvarchar(100),
	class nvarchar(100),
	section nvarchar(100),
)
go

insert into Info (name, class, section) values (N'Quoc Bao Dang', N'A', N'1th')
insert into Info (name, class, section) values (N'Ronaldo', N'B', N'2th')
insert into Info (name, class, section) values (N'Messi', N'E', N'5th')
insert into Info (name, class, section) values (N'Neymar', N'A', N'4th')
go