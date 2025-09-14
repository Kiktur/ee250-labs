# Lab 2

## Team Members
- Victor Gutierrez
- Angie Vasquez

## Lab Question Answers

## QA.1 - QA.3
Question 1: How did the reliability of UDP change when you added 50% loss to your local
environment? Why did this occur?

When 50% loss was added to the network environment when sending sequence 1-10 only some of the numbers showed up on the server like 1,3,6,9. The other numbers were missing this is because UDP does not retransmit lost packets, so any dropped messages never reach the server.

Question 2: How did the reliability of TCP change? Why did this occur?
When 1-10 was sent over TCP with 50% packet loss, all the numbers still arrived. This is because TCP ensures reliability by transmitting lost packets and using acknowledgments until every message is successfully delivered.

Question 3: How did the speed of the TCP response change? Why might this happen?
The TCP with loss was noticeably slower due because when TCP retransmits lost packets it has to wait for acknowledgements so there is more delay.

## QC.1 - QC.7
1. What is argc and \*argv[]?
  argc is the argument count. It's an integer that tells the program how many command line tokens(words) were typed when the program was run, this also includes the program name itself.
  argv[] is the argument vector. Its an array of C strings(chars*) which stores each of those arguments.

 2. What is a UNIX file descriptor and file descriptor table?
 A UNIX file descriptor is a small integer that processes use to access an open file or I/O resource.
 A file descriptor table is the list the Operating System keeps to map those numbers to the actual resources.

 3. What is a struct? What's the structure of sockaddr_in?
   A struct is a way to group variables in C.
   sockaddr_in stores an IPv4 socket address with fields for family,port, address, and padding.

4. What are the input parameters and return value of socket()
    The input parameters of socket() are domain, type, protocol and the return value is a file
	 descriptor(integer >= 0) if successful, or -1 on error.

5. What are the input parameters of bind() and listen()?
     bind() input includes socket fd, an address pointer, and its size.
	 listen() takes a socket fd and a backlog size.
       
6.  Why use while(1)? Based on the code below, what problems might occur if there are multiple simultaneous connections to handle?
       while(1) is like a loop running forever. while(1) keeps the server running so it can continuously accept new client connections. However, since this server handles clients one at a time, multiple simultaneous connections can cause blocking, delays, or dropped connections.

7. Research how the command fork() works. How can it be applied here to better handle multiple connections?
       fork() creates a new child process that runs as a copy of the parent. In this server, calling fork() after accept() lets that child process handle one client connection while the parent immediately goes back to accept() to wait for more clients. 
      So this allows multiple clients to be served at the same time instead of one by one.

This program makes several system calls such as 'bind', and 'listen.' What exactly is a system call?
 A system call is a way for a program to ask for the operating system's kernel to perform a service (like file or network access) that the program itself can't do directly.

 ## Question A.4 
 If you used LLMs for any part of this lab, explain how you used it.
 We used LLM to help explain topics not fully detailed in the lab handout like argc,file descriptors, and understanding how command fork() works.

