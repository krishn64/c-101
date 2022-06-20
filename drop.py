import dropbox


class Tranferdata:
    def __init__(self,access_token):
        self.access_token=access_token
    
    def upload_files(self,source,destination):
        dbx=dropbox.Dropbox(self.access_token)
        f=open(source,"rb")
        dbx.files_upload(f.read(),destination)
def main():
    access_token="sl.BJ5WbO938Kg3SN2rQrwaoamAgShH7QEhjUcRk6K-tbYnbEuYYwctPLT6vZKmFDlTBcqUTQ-e73aOoEgJtSWjexl9BLAsBJg-P3xtjLoeS9Kg07FsDYwJrvq1i1EBzxgQFV2A0iSZudDc"
    transferdata=Tranferdata(access_token)
    source=input("enter the file that is to be transfered")
    destination=input("where is will be droped off")
    transferdata.upload_files(source,destination)
    print("donezo gunzo")

main()


        