import ftplib
from get_file_size_ftp import openpyxl_ext


file_size_dict = {}


def get_files_size_recursively(base_directory, host, id, pw):
    global file_size_dict
    base_directory = base_directory
    host = host
    id = id
    pw = pw
    dir_list = []
    file_list = []
    with ftplib.FTP(host=host, user=id, passwd=pw) as ftpcon:
        ftpcon.cwd(base_directory)
        # ftpcon.retrlines('LIST')
        ftpcon.retrlines('LIST', lambda x=' ': dir_list.append(x.split(maxsplit=8)[8]) if x.startswith("d") else
                         file_list.append("{}\t{}".format(x.split(maxsplit=8)[4], x.split(maxsplit=8)[8])))
                        # file_list.append(x.split(maxsplit=8)[4])
        print("file list is {}".format(file_list))

        if len(file_list) > 0:
            for file in file_list:
                # file_path = "{}/{}".format(base_directory, file)
                # print("Getting size of file {}".format(file))
                # ftpcon.sendcmd('TYPE I')
                # file_size = ftpcon.size(file)
                #***Another way to get size***Start****#
                size_file = file.split("\t", maxsplit=1)
                file = size_file[1]
                file_path = "{}/{}".format(base_directory, file)
                file_size = size_file[0]
                #*********END************#
                file_size_dict[file_path] = file_size
    print("###################")
    print("dir list is {}".format(dir_list))

    if len(dir_list) > 0:
        for dir in dir_list:
            dir = "{}/{}".format(base_directory, dir)
            get_files_size_recursively(dir, host, id, pw)


def write_to_excel(file_size_dict_l: dict):
    wb = openpyxl_ext.Workbook()
    ws = wb.active
    ws.title = "result"
    row = 1
    ws.cell(row, 1, 'File_Path')
    ws.cell(row, 2, "File_Size")
    for file_path, file_size in file_size_dict_l.items():
        row += 1
        ws.cell(row,1, "{}".format(file_path))
        ws.cell(row, 2, "{} kb".format(int(file_size)//1024))
    wb.save("Result_file.xlsx")


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("host", help="Host of ftp server")
    parser.add_argument("user", help="Provide user id of the ftp server")
    parser.add_argument("password", help="Provide password for the ftp user")
    parser.add_argument("base_directory", help="Provide the base_directory")
    args = parser.parse_args()
    host = args.host
    user = args.user
    password = args.password
    base_dir = args.base_directory
    print(base_dir)
    print()
    get_files_size_recursively(base_dir, host, user, password)
    # get_files_size_recursively("/INCOMING/160958/15-16-part", "ftp.teoco.com", "ranftp", "7SxWPbKooh")
    write_to_excel(file_size_dict)






