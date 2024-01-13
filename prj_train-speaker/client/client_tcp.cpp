#include <winsock.h>
#include <iostream>

#define IP "192.168.3.63"
#define PORT 8080

// Convert a string into a char array
void str_to_char_arr(char* char_arr, int char_len, std::string msg) {
    strncpy(char_arr, msg.c_str(), char_len-1);
    char_arr[char_len-1] = 0;
}

// Close the program and display the given string
void error(std::string msg) {
    char err[100];
    str_to_char_arr(err, sizeof(err), msg);
	perror(err);
	exit(1);
}

// Close the socket connection
void close_connection(SOCKET s) {
    if (s)
        closesocket(s);
    WSACleanup();
}

// Create a socket connesion, return the socket
SOCKET connect_to_sever() {
    WSADATA wsadata;
    SOCKET s, connection;

    int startup = WSAStartup(MAKEWORD(2,2), &wsadata);
    if (startup)
        error("ERROR: WSAStartup failed");
    
    if (wsadata.wVersion != 0x0202) {
        close_connection(s);
        error("ERROR: wrong wsadata version");
    }

    SOCKADDR_IN server_addr;
    server_addr.sin_family = AF_INET;
    server_addr.sin_port = htons(PORT);
    server_addr.sin_addr.s_addr = inet_addr(IP);

    s = socket (AF_INET, SOCK_STREAM, IPPROTO_TCP);
    if (s == INVALID_SOCKET) {
        close_connection(s);
        error("ERROR: invalid socket");
    }

    connection = connect(s, (SOCKADDR *)&server_addr, sizeof(server_addr));
    if (connection == SOCKET_ERROR) {
        close_connection(s);
        error("ERROR: server connection failed");
    }

    return s;
}

void send_message(SOCKET s, std::string msg) {
    char arr_msg[1000];
    str_to_char_arr(arr_msg,sizeof(arr_msg),msg);
    send(s,arr_msg,sizeof(arr_msg)-1,0);
}

int main() {
    SOCKET s = connect_to_sever();
    send_message(s, "Test1");
    close_connection(s);
    
    std::cout << s << "\n";
}

// g++ client_tcp_2.cpp -o client_2 -lws2_32