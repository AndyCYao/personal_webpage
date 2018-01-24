title: "CMPT 383 Comparative Programming Language"
date: 2018-01-05
code: "CMPT 383"
semester: "Spring 2018"

Taught by Professor Toby Donaldson

### History of Programming Languages
Programming languages are developed organically based on the developer's needs. 

The three most influential languages were Fortran, LISP, and COBOL

__Fortran__ (1957), stands for Formula Translator, was the first language to incorporate variables, before this it was machine languages. John Backus developed this with engineering and science users in mind. Fortran is still actively used today.

__LISP__ (1958), stands for list processing, developed by John McCarthy is a language with a simple core, developed with math users in mind. 

__COBOL__ (1950's), asscoiated with Grace Hoppe, for business users, stands for Common Business Oriented Language. 

we briefly mentioned the below languages 

__Algol__ (1960's), was another pioneer language, but was not heavily adopted.

__SmallTalk__ (1970's), asscoiated with Alan Kay and XEROX parc, help popularized object oriented programming in North America. inspired by Simula and LISP

__Prolog__ (1970's), developed with logic in mind, for AI and parsing English, syntax is based on first order logic. 

### Ways to Organize Languages:
__Declarative vs Procedural__

Declarative languages like markup, SQL, prolog.

Procedural languages like Von Neuman (C Ada Fortran) , Object Oriented (java, smalltalk), or Script (python ruby perl)

__Compiled vs Interpretted__

Compiled programs (C, Fortran) are very efficient, compilers can find errors before program is run, and it can do static analysis (checking something against the soruce code)

Interpretted programs (like Python, LISP) are good for fast development, allow codes to be created on the fly, but it is slower than compiled codes

__Why use Go__

Developed at Google, a way to replace C++ for writing server, the developers thought C++ took too long to compile.

Go compiles fast, comparable to interpret languages.

__Concurrency Support__ has “Go routines” that are lightweight processes to handle concurrency tasks. 

__No Exceptions__ Go relies on explicit error codes return from functions. Whereas error handling in C++, java, leads to convoluted code that treats too many situations as error. Go forces you to explicitly deal with error. (No error you would return nil)

__Lightweight typing__ Go lets you leave off the type, but is still statically typed


__Novel use of interface__ Go does not have classes,but still object oriented by introducing interface 

__Closure__ allows passing functions (lambda functions)

___other notes on  Go___
Go has really modern set of libraries like __fmt__ thats relevant to web dev. 

**Go run** lets you compile and run in one step

if variables or functions are Uppercase, then its public, (other languages have a explicit "public for these things)

Go has a built in formatter (**Go fmt**) that conforms your code when you save

the `:=` initializes and gives values to a variable , the type is inferred

`name := ""`  

the above is similar to `var name string`, `name = ""` 

	:::code
	var name string
	fmt.Scanf("&s", &name) 
	// needs an address of name because Scanf writes in value at the name address

Go uses `for` for both `for` and `while` like in other languages

the for loop pattern is
	
	:::Go
	for i := 0l i < 10; i++ {
		//do stuff
	}
	
	//range loop
	s := "some string"
	for i,c := range s{
		//do stuff
		fmt.Printf("s[%v] = '%v'\n", i, c)	// the %v gets the unicode value, %c gets the char 
	}
	
the Go compiler says its an error if a variable is declared but not used, the aim is to make things practical by taking out superfluous variables

because of this, the `_` is a blank variable in Go, it allows the compiler to run if you dont care about a declared variable. 

__array__ is immutable in Go, problem is the length is part of the type.

__slice__ is a dynamic array , builds ontop of an array

`var sl []int = []int{1,2,3}` gives starting values to the sl slice

alternatively `sl := []int{1,2,3}`

we can use the builtin keywords `append` and `make` to generate slices

__map__ is declared like `var notes map[type of key] type of value` the string is the type of the key, and int value

Go returns a value 0 if a key is not there in the map. different from how other languages does it. 

`panic` is for error checking, and panic immediately ends the program 

Go didn't add `destructors`, instead, the `defer` keyword allows statements to run after function ends, effectively Go programmers adds `deferobject.close()`

--

Go does not have inheritence, instead, it has concept of embed. so if structA  has structB inside, and structC. StructA is of a separate type than structB and structC.


need to understand how Go methods and functions interact with __method sets__ 

in __Go__, some key words are bound at language design time, and  can't be unbound, like __For loop__ 

There are two binding time

__Compile Time Binding (Static Binding)__ vs __Runtime Binding (Dynamic Binding)__

different languages decide on the binding differently, runtime binding gives more flexibility, while compile time binding lets you find mistakes much faster.

Go, C++, Java, Haskell -> are all compiled time binding  languages,

Javascript, Python, Ruby, Scheme/Lisp -> are all binding done at runtime. 

the bindings are not all distinct like this, all languages implement a mix of both


#### Memory Allocation

Static  -> compile time - eg. global variable , the original Fortran only had static memory variables. but problem is, when we start using functions, we want functions to have their own local variables. so static allocated programs had a hard time accomodating for local variables. which leads to... 

Stack (or call stack)  -> is created in run time, each stack contains __stack frame__ that stores the local variables at the current function.and automatically pop when the function exits.   


Heap ( dynamic) 


__Summary Of Go__
easy language for getting a job, write a web server etc. 


