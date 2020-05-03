COMMAND LINE Arguements:
This program takes "FTP/Sftp-host" "FTP-user"  "password"  "base_directory at FTP server" port 

 
USAGE:
get_file_size_ftp_sftp.exe host user  password  base_directory  port
create a .bat file with the above command for easy to run.

FUNCTIONALITY:
Based on Port value, it consider the server protocol. If port is other than 21 then it is consider as SFTP server.

It travers through all the directories and files under the base_directory, get thier size, 
Then it creates a file named "result_file.xlsx" at current directory from where the program was fired.
and store that files-path and their size into it.

positional arguments:
  host            Host of ftp server
  user            Provide user id of the ftp server
  password        Provide password for the ftp user
  base_directory  Provide the base_directory
  port 			  Provide the port number to which the ftp/sftp server is exposed.
  
