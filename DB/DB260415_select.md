# 26 04 29

## CREATE
```sql
create table DEPT (
	id interger auto increment primary key,
	name text not null unique
);
```

### AUTO INCREMENT, PRIMARY, UNIQUE, NOT NULL 
-- schema 생성시
auto increment primary key;
not null unique;

## ALTER 
```sql
alter table tb 
add money interger;
```

- sqlite에선 alter ~~ modify 지원 안 됨

## INSERT
```sql
insert into EMP (name) values('Bob'),('Billy'),('Van');
```
## UPDATE
```sql
update EMP set dno=1 where name='Slave';
```

## DROP
```sql 
drop table DEPT
```

## SELECT


## Reference
- [https://www.w3schools.com/sql/default.asp](https://www.w3schools.com/sql/default.asp)

# 트리거(Trigger), 주장(Assertion)

# 내포/내장된 SQL (Embedded SQL)



```
[[1][2][3]]
[[id name] [1 A] [2 B] [3 C]]
id name
1 A
2 B
3 C

>> 
1 
2 
3
[[[1 2] 2][2 3][3 4]]
>>
1 2
2 
2 3
3 4
[[1 [2 3]][2 3][3 4]]
>>
1 2
  3
2 3
3 4
```