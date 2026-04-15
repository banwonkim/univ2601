
# SELECT 

```sql
$ATT=ATTRIBUTE
$REL=RELATION
$COND=CONDITION

SELECT [DISTINCT] $ATT
FROM $REL
[WHERE $COND 
	[?]]

[GROUP BY $ATT]
[HAVING $COND]
[ORDER BY $ATT [ASC | DESC]];
```

## SELECT EXAMPLE
### 1 BASIC
$RNAME = DEPTTABLE

|NO | NAME|
|---|---|
|1 | 영업 |
|2 | 기획 |
|3 | 쓰레기|
|4 | 노예 |

```sql
SELECT NO, NAME
FROM DEPTTABLE 
```

### 2 DISTINCT 

$RNAME : EMP
| TITLE |
| :--- |
| CEO |
| CEO |
| MANAGER |
| MANAGER |
| LABOR |
| SLAVE |
| SLAVE |

```sql
SELECT DISTINCT TITLE
FROM EMP
```
| TITLE |
| :--- |
| CEO |
| MANAGER |
| LABOR |
| SLAVE |

 
### 3.0 WHERE 

```SQL
SELECT *
FROM EMP
WHERE NO=2
```

| EMPNO | NAME | DNO |
| :--- | --- | --- |
| 123 | B | 2 |
| 456 | C | 2 |

```SQL 
SELECT EMP 
FROM GUY
WHERE NAME LIKE 'B%';
```


|NAME|NO|
| :--- | --- |
|BILLY|1|
|BUNNY |2|


### 3.1 WHERE2

|NAME|EMPNO|MONEY|
| :--- | --- | --- | 
|A|1|100|
|B|3|200|
|C|3|500|
|D|3|400|

```sql
SELECT NAME,MONEY
FROM TABLE
WHERE MONEY>300 AND EMPNO=3;
```

### 4 잘못된 질의 
```SQL
--WRONG
WHERE NAME='SHIT' AND NAME='DIRTY' 

-- ANSWER1
WHERE NAME='SHIT' OR NAME='DIRTY' 

-- ANSWER2
WHERE NAME IN ('SHIT', 'DIRTY')
```

우선순위 
|OP|ORDER|
| :--- | --- | 
|비교 연산자|1|
|NOT|2|
|AND |3|
|OR|4|

### 5 BETWEEN
```SQL
WHERE MONEY BETWEEN 300 AND 500;
WHERE MONEY >= 300 AND MONEY <= 500;
```
|NAME|MONEY|
| :--- | --- | 
|A|350|
|B|450|

### 6 IN
```sql
SELECT NAME, NO
FROM EMP
WHERE NO IN (1,3);
```

|NAME|NO|
| :--- | --- | 
|A|1|
|B|3|
|C|2|



|NAME|NO|
| :--- | --- | 
|A|1|
|B|3|


### 7 OP

```sql
SELECT NAME, MONEY, MONEY*2 AS NEWMONEY
FROM EMP
WHERE NO=2;
```
|NAME|MONEY|NEWMONEY|
| :--- | --- | --- | 
|A|300|600|
|B|120|240|
|C|200|400|


### 8 NULL
```sql
SELECT NAME, MONEY, MONEY*2 AS NEWMONEY
FROM EMP
WHERE NO IS NULL;

-- WRONG
WHERE NO=NULL;

-- RES : ALL FALSE
NULL > 300
NULL = 300
NULL <> 300
NULL = NULL
NULL <> NULL


```

### 9 UNKNOWN

- **AND**

| |T|F|U|
|---|---|---|---|
|T|T|F|U|
|F|F|F|F|
|U|U|F|U|

- **OR**

| |T|F|U|
|---|---|---|---|
|T|T|T|T|
|F|T|F|U|
|U|T|U|U|
