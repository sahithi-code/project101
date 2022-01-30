import os
import dropbox
from dropbox.files import WriteMode

class TransferDAta:
    def __init__(self,access_token):
        self.access_token = access_token
    def _uploading_Files(self,file_from,file_to):
        dbx=dropbox.Dropbox(self.access_token)
        for root , dirs ,files in os.walk(file_from):
            for filename in files:
                local_path = os.path.join(root , filename)

                relative_path = os.path.relpath(local_path,file_from)
                dropbox_path = os.path.relpath(file_to,relative_path)

                with(local_path,'rb') as f:
                    dbx.files_upload(f.read(),dropbox_path, mode=WriteMode('overwrite'))

def main():
    access_token  = 'sl.BBER4ymedz3Xe-tlAE5j-HTUfu9ILSwMUizp824vNLua5UHlbKA13TrcjjI5G2HoBP5r8Ebrs_xyxI0JBi-EyOAh42o3_Kr08W-jR3jzwMKeS-XwaghbevlPH6psQYuIBYQW4RcJ'
    transferData = TransferDAta(access_token)
    file_from= input('enter the path of the folder to transfer: ')
    file_to = input('enter the full path to upload to dropbox:  ')
    transferData.upload_file(file_from,file_to)
    print("file has been moved !!!")
main()
    

        