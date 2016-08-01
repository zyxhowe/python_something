import crypt
dict_file_name=raw_input("dict file:")
password_file=raw_input("password file:")
pwd_file=open(password_file,'r')

for a in pwd_file.readlines():
        if a.find('$') != -1:
                b=a.split(':')
                name=b[0]
                encrypt=b[1]
                c=encrypt.split('$')
                slat='$'+c[1]+'$'+c[2]+'$'
                dictfile=open(dict_file_name,'r')
                for pd in dictfile.readlines():
                        pd=pd.strip('\n')
                        test_encrypt=crypt.crypt(pd,slat)
                        if test_encrypt==encrypt:
                                print name+' passwd is '+pd
								break;
