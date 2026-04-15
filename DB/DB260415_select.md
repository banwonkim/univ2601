
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
- 1
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

- 2 DISTINCT 

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


- 3 WHERE 

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

- 4 잘못된 질의 
```
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
