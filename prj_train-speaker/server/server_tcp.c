#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <unistd.h> 
#include <string.h>

#define PORT 8080
#define FILE_PATH "./trains.txt"

void error(char *msg) {
	strcat(msg,"\n");
	perror(msg);
	exit(1);
}

int init_server() {
	int sock_fd;
	struct sockaddr_in serv_addr;
	
	sock_fd = socket(AF_INET,SOCK_STREAM,0);
	if (sock_fd < 0) {	
		error("ERROR: socket opening failed");
	}
	memset(&serv_addr, 0, sizeof(serv_addr));
	
	serv_addr.sin_family = AF_INET;
	serv_addr.sin_addr.s_addr = INADDR_ANY;
	serv_addr.sin_port = htons(PORT);
	
	int bind_suxceed = bind(sock_fd, (struct sockaddr*) &serv_addr, sizeof(serv_addr));
	if (bind_suxceed < 0) {
		error("ERROR: binding failed");
	}
	return sock_fd;
}

void recv_message(int connection_fd, char* empty_msg) {
	memset(empty_msg, 0, sizeof(empty_msg));
	int read_suxceed = read(connection_fd,empty_msg,256);
	if (read_suxceed < 0) {
		error("ERROR: reading error");
	}
}

int process_line(char *line, char *key, char *value) {
	char g_key[200], g_value[200], *token;
	const char sep[] = ":";
	
	token = strtok(line,sep);
	strcpy(g_key,token);
	
	token = strtok(NULL,sep);
	strcpy(g_value,token);
	
	if (strcmp(key,g_key) == 0) {
		strcpy(value,g_value);
		return 1;
	}
	strcpy(value,"nf");
	return 0;
}

int get_respective_string(char* empty_value, char* key) {
	int ch_int;
	char ch[2], line[200];
	FILE *fp;
	
	ch_int = 0;
	ch[0] = 0;
	ch[1] = 0;
	strcpy(line,"");
		
	fp = fopen(FILE_PATH, "r");
	if (fp == NULL) {
		char err[100];
		sprintf(err, "ERROR: unable to open %s", FILE_PATH);
		error(err);
	}
	
	char value[200] = "";
	while (1) {
		char line[200] = "";
		while (1) {
			ch_int = fgetc(fp);
			ch[0] = (char) ch_int;
			if (ch_int == EOF || ch[0] == '\n') {
				int res;
				res = process_line(line,key,value);
				if (res) {
					strcpy(empty_value,value);
					fclose(fp);
					return 1;
				}
				break;
			}
			strcat(line,ch);			
		}
		if (ch_int == EOF)
			break;
	}
	
	strcpy(empty_value,"invalid key");
	fclose(fp);
	return 0;
}

void send_answer(int connection_fd, int found) {
	char answer[5];
	strcpy(answer,found ? "ack":"nack");
	printf("%s\n",answer);
	write(connection_fd,answer,strlen(answer));
}

void start_deamon(int sock_fd) {
	int connection_fd, key_found;
	struct sockaddr_in client_addr;
	
	while (1) {
		listen(sock_fd,5);
		int client_len = sizeof(client_addr);
		connection_fd = accept(sock_fd, (struct sockaddr *) &client_addr, &client_len);
		if (connection_fd < 0)
			error("ERROR: client connection dennied");
		char msg[200];
		recv_message(connection_fd,msg);
		char value[200];
		key_found = get_respective_string(value,msg);
		send_answer(connection_fd, key_found);
		// printf("PLAY: %s\n",value);
		char output[200];
		sprintf(output,"python3 text_to_speech.py %s",value);
		system(output);
	}
}

int main() {
	int s = init_server();
	start_deamon(s);
	return 1;
}
