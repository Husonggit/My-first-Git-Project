#include <unistd.h>
#include <stdio.h>
#include <sys/stat.h>
#include <fcntl.h>

int main()
{
	#define MAX_READ 2040
	ssize_t numRead;
	char buffer[MAX_READ];

	int fd = open("./file", O_RDWR);
	if (fd == -1)
	{
		printf("open error %d\n", fd);
		return -1;
	}

	numRead = read(fd, buffer, MAX_READ);
	if (numRead == -1)
		return -1;

	buffer[numRead] = '\0';
	printf("The input data was : %s\n", buffer);

	close(fd);
	return 0;
}
	
