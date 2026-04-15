
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

## DISTINCT 

$RNAME : EMP
```
-----
TITLE
-----
CEO
CEO 
MANAGER
MANAGER
LABOR
LABOR
SLAVE
```

```sql
SELECT TITLE
FROM EMP
```
```
-----
TITLE
-----
CEO
MANAGER
LABOR
SLAVE
```
