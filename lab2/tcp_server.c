/* A simple server in the internet domain using TCP
 * Answer the questions below in your writeup
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h> 
#include <sys/socket.h>
#include <netinet/in.h>

void error(const char *msg)
{
    perror(msg);
    exit(1);
}

int main(int argc, char *argv[])
{
    /* 1. What is argc and *argv[]?
     * argc is the argument count. It's an integer that tells the program how many command line tokens(words) were typed when the program
	 was run, this also includes the program name itself.
     argv[] is the argument vector. Its an array of C strings(chars*) which stores each of those arguments.
     */
    int sockfd, newsockfd, portno;
    /* 2. What is a UNIX file descriptor and file descriptor table?
     * A UNIX file descriptor is a small integer that processes use to access an open file or I/O resource.
	 A file descriptor table is the list the Operating System keeps to map those numbers to the actual resources.
     */
    socklen_t clilen;

    struct sockaddr_in serv_addr, cli_addr;
    /* 3. What is a struct? What's the structure of sockaddr_in?
     * A struct is a way to group variables in C.
	 sockaddr_in stores an IPv4 socket address with fields for family,port, address, and padding.
     */
    
    int n;
    if (argc < 2) {
        fprintf(stderr,"ERROR, no port provided\n");
        exit(1);
    }
    
    sockfd = socket(AF_INET, SOCK_STREAM, 0);
    /* 4. What are the input parameters and return value of socket()
     * The input parameters of socket() are domain, type, protocol and the return value is a file
	 descriptor(integer >= 0) if successful, or -1 on error.
     */
    
    if (sockfd < 0) 
       error("ERROR opening socket");
    bzero((char *) &serv_addr, sizeof(serv_addr));
    portno = atoi(argv[1]);
    serv_addr.sin_family = AF_INET;
    serv_addr.sin_addr.s_addr = INADDR_ANY;
    serv_addr.sin_port = htons(portno);
    
    if (bind(sockfd, (struct sockaddr *) &serv_addr,
             sizeof(serv_addr)) < 0) 
             error("ERROR on binding");
    /* 5. What are the input parameters of bind() and listen()?
     *  bind() input includes socket fd, an address pointer, and its size.
	 listen() takes a socket fd and a backlog size.
     */
    
    listen(sockfd,5);
    clilen = sizeof(cli_addr);
    
    while(1) {
        /* 6.  Why use while(1)? Based on the code below, what problems might occur if there are multiple simultaneous connections to handle?
        * while(1) is like a loop running forever. while(1) keeps the server running so it can continuously accept
		new client connections. However, since this server handles clients one at a time, multiple simultaneous connections
        can cause blocking, delays, or dropped connections.
        */
        
	char buffer[256];
        newsockfd = accept(sockfd, 
                    (struct sockaddr *) &cli_addr, 
                    &clilen);
	/* 7. Research how the command fork() works. How can it be applied here to better handle multiple connections?
         * fork() creates a new child process that runs as a copy of the parent. In this server, calling fork() after accept()
		 lets that child process handle one client connection while the parent immediately goes back to accept() to wait for more clients. 
         So this allows multiple clients to be served at the same time instead of one by one.
         */
        
	if (newsockfd < 0) 
             error("ERROR on accept");
	bzero(buffer,256);
        
	n = read(newsockfd,buffer,255);
        if (n < 0) 
            error("ERROR reading from socket");
            printf("Here is the message: %s\n",buffer);
        n = write(newsockfd,"I got your message",18);
        if (n < 0) 
            error("ERROR writing to socket");
        close(newsockfd);
    }
    close(sockfd);
    return 0; 
}
  
/* This program makes several system calls such as 'bind', and 'listen.' What exactly is a system call?
 * A system call is a way for a program to ask for the operating system's kernel to perform a service (like file or network access) that the program itself can't do directly.
 */
