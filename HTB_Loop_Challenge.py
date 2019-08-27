import sys
import zipfile
import optparse
from threading import Thread

# Unzipper Function
def extractFile(zname):
    try:
        zFile = zipfile.ZipFile(zname) 
        file_info =  zFile.infolist()
        filename =  file_info[0].filename
        password = filename.split(".")
        zFile.extractall(pwd = password[0])
        print "The file " + zname + " successfully extracted with password " + password[0]
        last_file = filename
        extractFile(filename)
        
        
       
    except:
        print "The script has either failed or completed"
        print "The last file that was unzipped was " + zname
    
        
def main():
    parser = optparse.OptionParser('usage: zipcracker.py ' + '-f <zipfile>')
    parser.add_option('-f', dest='zname',type='string',help='specify zip file')
    (options,args) = parser.parse_args()
    if (options.zname == None):
        print parser.usage
        exit(0)
    else:
        zname = options.zname
    extractFile(zname)

if __name__ == '__main__':
    main()
