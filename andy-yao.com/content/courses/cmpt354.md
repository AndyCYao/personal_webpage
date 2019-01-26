title: "Database Management"
date: 2017-03-01
semester: "Spring 2017"
code: "CMPT 354"

### CMPT 354 Database Management Winter 2017

### ER Diagrams and Relational Diagram 
*ER Diagrams* are for concepts, it is used for abstract grouping of entities and relationships
*Relational Diagram* is for logical modeling, tends to be drawn when the ER Diagram is already fleshed out.

### Entity 
Weak entity are those that depends on a foreign entity to identiy itself. AKA child entity that depends on the parent entity

Strong entity, those that have their own primary key

### Covering Constraint and Overlap Constraint
Pertains to the ISA relation.
*Covering Constraint* - Does every Employee have to be a contractor, or temp?
*Overlap Constraint* - Can contractor or temp overlap? ie. Can the employee be both

### Keys
- Super key are set of candidate keys.
- Candidate keys are column or columns that uniquely identifies the entries in an entity
- Primary key is the minimal candidate key. 

### Database 
- This is a physical storage of data, we will be installing relational databases, which is a part of DBMS (database management system)

- The purpose of a DB is to faciliate access/ storing data. key things to note is to protect data from concurrent users, crash recoveries, etc. 

- a schema is a way to describe data

### SQL
- we have DDL, data definition language, which are the CREATE, DROP, DELETE, keywords
- DML, data manipulation language, which includes
	keywords such as SELECT, UPDATE, DELETE etc. 

### ACID
- Databases must maintain 'ACID'
- Atomic - groups of transaction must all pass or all fail, if fail, a log is used to unroll the changes. 
- Consistent - After each transaction, the DB is in consistent state.
- Isolation - Concurrency control to allow multi user
- Durability - the database must not be corruptible and lose information

For example 

	:::sql
	INSERT INTO tableName(a, b, c, d)
	VALUES (1,2,3,4)
	CREATE VIEW ViewName 
	(SELECT ...)
	DROP VIEW
	LIKE (case insensitive)
	UNION - joins two select queries, note fields have to be the same
	INTERSECT - 
	EXCEPT


Relational Algebra's Set division can be translated to SQL like so

e.g.  Find sailors who’ve reserved all boats

	:::sql
	SELECT  S.sname
	FROM  Sailors S
	WHERE  NOT EXISTS 
	    ((SELECT  B.bid
	      FROM  Boats B)
	        EXCEPT
	            (SELECT  R.bid
	               FROM  Reserves R
	               WHERE  R.sid=S.sid))


Find Entity that have only 1 attribute
e.g. Find the snames of suppliers who supply only red parts.

	:::sql
	Select S.sid from Suppliers S
	where ‘Red’ = ALL (select Parts.color 
			from Catalog, Parts
			where Catalog.sid = S.sid and Parts.pid = Catalog.pid )

and 

	a = Any {a,3} 	True
	a = All {a,3} 	False
	a = Any {}		False
	a = All	{}		True

## Exam 2 Prep Notes

### Aggregate Operators
Operates on tuple sets, keywords include 
- COUNT(), 
- COUNT(DISTINCT())
- SUM()
- AVG()
- MAX()
- MIN()
Note when doing aggregation, need to include 'GROUP BY' keyword

the HAVING keyword acts as a filter to the aggregate clause. 

### Null Values
can be interpreted as 
- Value Unknown(eg, rating has not yet been assigned)
- Value inapplicable ( no spouse's name)
- Value withheld (phone number)

Rule For Null:
- an arithmetic operator with at least one NULL argument always returns NULL
- Comparison of a NULL value to any second value returns a result o UNKNOWN
therefore, a selection returns only these tuples that makes the condition in the WHERE clause TRUE, those with unknown or false do not qualify. 
As part of 3 value logic (Ture False Unknown)

	TRUE AND UNKNOWN = UNKNOWN
	FALSE AND UNKNOWN = FALSE
	FALSE OR UNKNOWN = UNKNOWN
	NOT UNKNOWN = UNKNOWN

as well, 

	:::sql
	SELECT * 
	FROM t1
	WHERE col_1 > 5
	OR col_1 < 5
	OR col_1 = 5


Any record where col_1 has NULL will not be returned in the above query

### Outer Joins
SQL outer joins include NULL values

	:::sql
	SELECT *
	FROM a LEFT OUTER JOIN b
	ON a.id = b.id

LEFT OUTER JOIN would show dangling tuples from left input table. (null is filled for all attribute of right input)

RIGHT OUTER JOIN does the same but from right table's perspective

FULL OUTER JOIN shows dangling tuples from both input table

### Security 

	:::sql
	-- ex1
	GRANT SELECT, INSERT, DELETE 
	ON Reserves 
	TO Yuppy 
	WITH GRANT OPTION
	-- ex2
	GRANT UPDATE(rating) ON Sailors TO
	Leah

user yuppy can now select, insert, and delete, and also grant other people these privileges. 

user leah can now update ratings, but can't gran this privilege to other. 

### View
use view when you want more control on whether the user can read, write, execute depending on authorization level.

View is a relation that is stored for use later. 

### Integrity Constraints CHECK and ASSERTION
Types of IC include:
- Domain Constraint (field values must be right type, always enforced)
- Attribute based CHECK (defined in declaration of an attribute, activate on insertion)

	:::sql
	CREATE TABLE ..
	... CHECK (col_1 >= 1 AND col_2 <= 30)
	# can also name the check 
	CREATE TABLE ...
	CONSTRAINT noFoo
	CHECK('Foo' <> ANY(SELECT ...))

	
- Tuple-Based Check (defined in declaration of table, activate on insertion to corrosponding table or update of tuple) 

		:::sql
		CREATE TABLE ...
		... CHECK(colA >= colB)

- Assertion: (defined independently from any table, activate on any modification of any table mentioned in assertion)

		:::sql
		CREATE ASSERTION notTooManyReservations
		CHECK (10 > ALL (SELECT COUNT(*)
						FROM Reserves
						GROUP BY sid))

Checks and Assertions are not well supported in SQL.

Check is not in SQL SERVER

Assertion is not supported in postgresSQL

### Triggers
procedures that starts automatically if specificed change occurs in the DBMS.
has 
- Event (activates the trigger)
- Condition (tests whether trigger should run)
- Action

	:::sql
	CREATE TRIGGER youngSailorUpdate
	    AFTER INSERT ON SAILORS			/* Event */
	    REFERENCING NEW TABLE NewSailors	
	    FOR EACH STATEMENT
		   INSERT					/* Action */
			INTO YoungSailors(sid, name, age, rating)
			SELECT sid, name, age, rating
			FROM NewSailors N
			WHERE N.age <= 18;
	-- Referencing include
	NEW TABLE
	OLD TABLE
	OLD ROW
	NEW ROW
	--- Use begin and end to include multiple SQL Statements

the above inserts young sailors into separate table. 

### Trigger Vs General Constraints
Triggers can be activated in one SQL statement, but with arbitrary order,
trigger can activate other triggers.

trigger is more general than constraints, it can be used to monitor integrity constraints, construct a log, gather database stats. etc. 

### Application Dev. 
we can connect our application to a database through librarys with database calls (API).

We would pass SQL string to the API, must include a statement to connect to the right database. 

Connecting to Database Flow Chart 
- Load Driver (do this once)
- Driver Manager (do this once)
- Connection (do this once)
- Statement (repeatable)
- Query = String (repeatable)
- Cursor, Result (repeatable)

### Cursor
Since we don't know before hand how many records we fetch (a priori) SQL uses a mechanism call *cursor* to handle row selection

SQL Standard, Stored Procedure PSM  Term is Cursor 
Java Term is ResultSet
Visual Studio Term is DataReader

### Stored Procedure
written in general purpose programming language (Persistent stored modules PSM), and executed within the DBS. This extends SQL by basic concepts of a general purpose programming language. 

#### Impedance Mismatch
Since SQL is a declarative language while C and other language are procedural. there is different approach as to how data is handle, leading to unnecessary effort. Problem is trying to fit object oriented program into relational database. 

	:::sql
	-- Sample create procedure
	CREATE FUNCTION rateSailor (@sailorId INT)
	  RETURNS INT
	AS
	BEGIN
	DECLARE @numRes INT
	DECLARE @rating INT
		SET @numRes = (SELECT COUNT(*)
	                   FROM Reserves R
	                   WHERE R.sid = @sailorId)
	IF @numRes > 10 
	   SET @rating = 1
	ELSE
	   SET @rating = 0
	RETURN @rating
	END
	GO;
	SELECT dbo.rateSailor(22); go
	-- Can call a function
	EXEC SQL CALL functionName(@sid, @rating) 



### Advantage of Stored Procedure 
- encapsulates application logic while staying close to the data.
- different users can run the same logic 
- does not need cursor
- provides data security

### Internet App.
3 tier architecture , each tier can be independently maintained. 
- Presentation Layer -> HTML, CSS, Javascript, adapt to different display devices
- Middle Tier -> CGI , application server, (not emphasis in course)
- Database -> DB2, SQL Server

#### Thin Client and Thick Client Work Division
##### thin client 
only does graphic user interface. the business logic, data management depends on the server 

##### thick client. 
implements both graphic and business logic. while server implements data management

Downside -> server has to trust client, has scalability issue. hard to update all clients. 

### HTTP Hypertext Transfer Protocol 
1. client(browser) sends HTTP request to server 
2. server receives request and replies 
3. Client receives reply, makes new request
	
	GET ~/index.html HTTP/1.1 -- Request Line
	User-agent: Mozilla/4.0   -- Type of client
	Accept: text/html, image/gif, image/jpeg 

HTTP is stateless, every message is self contained. fires and forget. the advantage of this is don't need memory management. good for static information

Disadvantage is, no shopping baskets, user logins, dynamic content, and security is harder to implement.

#### Maintaing State, Client state or Server Side State
1. Server Side 
- Maintains data in a database, but requires database access to query or update. 
- Or stays in the application layer local memory. 
- this is used to persist old customer orders, click trails, user's movement etc. 
2. Client Side
- stores in cookies, the cookie is passed with every HTTP request. is a collection of (Name, Value) pair
- use cookies to store current user information, current shopping basket, non permanent choices

In a typical website:

- User logins are kept in cookies 
- User shopping basket kept in another cookie 
- User purchased information and credit card info are kept in server database. 
- Uer click streams are kept in a log on the web sever. 

#### HTTP Response
1. 200 OK Request Success
2. 400 Bad Request, request could not be fulfilled 
3. 404 Not Found,  does not exists
4. 505 HTTP Version Not Supported

### HTML Forms
	<FORM ACTION=“page.jsp” METHOD=“GET”
			NAME=“LoginForm”>
	…
	</FORM>

in the above, Action is the specific URI that handles the content 
Method -> HTTP GET or POST method
NAME -> name of the form. 

### Javascript 
adds functionality to the presentation tier. 

### Semi Structured Data and XML
XML is designed for used by applications, and work across different applications. it uses a digraph to handle the database. the leaf nodes represent the attribute data of some atomic type, while interior nodes represent complex objects. 

XML is ordered, S.S.D is not 

XML can mix text and element, has attributes, entities, processing instruction, comments, SSD does not. 

Labels indicate the relationship between two nodes. 

the graph does not need to be a tree structure, but is usualy acyclic. 

Object Exchange Model (OEM)
-separates complex object by building them from atomic object

#### XML Syntax #### 

	<BOOK genre= 'Science' format = 'Hardcover'>..data...</BOOK>

BOOK is the tag element , genre is the attribute, 'science' is attribute value

there can be zero or more attribute to every element.
![XML Tree]({{ site.url }}/images/XMLTree.jpeg)

#### XML VS Relational Databases ####

*Structure* RD uses table, XML is tree/ hiearchal graph
*Schema* RD has fixed schema, XML is flexible, self describing
*Queries* RD has SQL, XML has XPath, which is more complicated. 
*Ordering* RD has no order, XML order is implied
*Implementation* RD has native implementation, XML is add on. 

### XPath ###
is a query language for describing XML, uses tags to traverse through XML tree , and return series of qualifying items. 

	:::xml 
	path expression starts with '/'
	/tag1/tag2 return 
	this returns the set of tags that has /tag1/tag2 
	attributes - use @id to filter by tag id 
	<bib>
		<book bookID = 'b100'></book>
	</bib>
	/bib/book/@bookID 
	returns sequence 'b100'...
	/bib/*[publisher = 'McGraw']
	returns tags that have values Mcgraw
	use * to indicate wildcard
	// is for descendants. 
	note, /bib/*/title and /bib//title is the same 
	/bib/*[publisher = 'McGraw']
	/bib/book[2]/author[1] second paper, first author. 
	/bib/(paper | book) find title of each element that is a paper or a book. 


Exam 3 Prep

### File and Access Method
DBAs need to know how to configure a database for faster queries. 
Two issues

1. What plans are considered for a given query
2. Algoirthm to search for the cheapest plan
3. How is the cost of the plan estimated.

### Data On External Storage
Options include

1. Disks - can retrieve random pages at fixed cost, reading several consecutive pages is much cheaper than reading them in random order.

2. Tapes can read only in sequence

### Cost Model for Database operation 
terminologies:
B = # of data pages 

R = number of records per page 

D = average time to read and write (this time tends to dominate H, D average is 15 msec, H is 100 nano seconds.) 

C = average time to process a record 

H = time to apply a hash function.

### Alternative File Organization
Heap - suitable if typical access is file scan retrieving all records (unsorted) 

Need to scan for most operations (costly), insert is fast, just insert at end of file.

Sorted Files - suitable for retrieve in some order, or only a range of records is needed (note can only be sorted by one field)

cost of binary search is $$ log_2{# of disk pages} $$

Index - DS organize record via trees or hashing. 

#### To Find data entry 
Hash - constant cost for hash index 
Tree - log(height of the tree)

#### To find records that matches data entries 
Unclustered index #pages = # matching records 

Clustered Index - # matching pages. 

### Operations
Scan -> fetch all records in the file , the pages fetch from disk to the buffer pool 

Search With Equality Selection -> 'Find student records for students with ID ' = 23 

Insert -> identify the page in which record must be inserted, fetch that page from disk, modify it to include new record, write back to modified page. 

Delete -> must identify the page that has the record, fetch from disk, modify it, write it back. 



### Index
Pro- Are optional structure associated with a table which may improve the performance of a query.
Indices increase the speed of join (because foreign keys can be indexed too)

primary vs. secondary - search key contains primary key, then called primary index.


Con- Indices needs to be updated everytime there is an update. 

- Clustered Index (Alternative 1) Data Entry = Data Record (AKA Covering Index)

the data and the index is together, think phone book, which is organized by ascending phone numbers, usually the primary key of a table is in clustered

we can only have *one* clusterd index, b/c the table cannot be sorted by multiple columns. 

index + sorted file is the best.
Called clustered index.

- Non-Clustered Index. (Alternative 2 and Alternative 3)

this means data is not where the record is. think textbook, with a index at the back. The two are separate,  the index record  *points* to the data entry, relevant section in the textbook. 

we can have multiple non clustered indices, since they are separated objects. 

data entries are much smaller than data records.so better than alternative 1.

While alternative 3 is more compact than 2, it is variable sized data entries (dont know how long it can get, if the search key is common occurence.)

(to build a clustered index, you would need to sort the heap file and also keep index sorted)

	:::sql
	--Alternative 2 looks like 
	color, location
	red, 1
	red, 3
	red, 2
	blue,6
	blue, 4
	blue, 5
	--Alternative 3 looks like
	red 1,2,3
	blue 4,5,6


#### Hash Base Index
Used for equality search. index is a collection of buckets, and buckets are primary page plus zero or more overflow page. 

If alternative 1 is used, the buckets contain the data record. 

with alternative 2, bucket contains <key,rid> pairs

with alternative 3, bucket contains <key, rid list> pairs

Assumes 80% page ocupancy

#### B Tree Index

leaf pages contain the data enry and *are chained*
that means they can visit previous and next. 

non-leaf pages contain index entries, they direct searches. 
 
Assumes 67% page occupancy

### Query optimizer (Chap 13 of Database Management System)
the conjuncts that the index matches as the primary conjuncts in the selection. 

hash index matches a selection condition containing no disjunctions if there is a term of the form *attribute = value * for each attribute in the index search key 
tree index matches a selection condition containing no disjunctions if there is a term of the form attribute *op* value for each attribute in a prefix of the index's search key. 



#### System R Optimizer
Is a type of query optimizer, works well for <10 joins. 

key features, 

1. the use of statistics about the database instance to estimate the cost of a query evaluation plan. 
2. Consider only plans with binary joins which the inner relation is base. 
5. Model of costs that accounts fo CPU cost as well as I/o Cost 

		:::sql
		SELECT s.sname
		FROM Reserves R, Sailors S 
		WHERE R.sid = S.sid 
		AND R.bid = 100 AND S.rating > 5


the above can be broken in the form of RA expression tree.
can be broken down in 

To obtain the evaluation plan, we need to implement each relational algebra operation. for example, a JOIN between Reserve and Sailor is a page oriented simple nested loop. The projection and selection commands are 'on the fly' generated. 

In a RA expression tree, each internal node are relational algebra operator, and each leaf is a table. 

*Key Takeaway - Pushing Selections* since JOIN operations are expensive, it is better to apply selections early, so that the size of the tables been joined is reduced.  



