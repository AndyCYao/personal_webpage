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

__Concurrency Support__ has “go routines” that are lightweight processes to handle concurrency tasks. 

__No Exceptions__ Go relies on explicit error codes return from functions. Whereas error handling in C++, java, leads to convoluted code that treats too many situations as error. Go forces you to explicitly deal with error. (No error you would return nil)

__Lightweight typing__ Go lets you leave off the type, but is still statically typed


__Novel use of interface__ Go does not have classes,but still object oriented by introducing interface 

__Closure__ allows passing functions (lambda functions) 
