import os
import dropbox

class TranseferData:
    def __init__(self,access_token):
        self.access_token = access_token
    
    def upload_files(self,file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)
        for root, dirs, files in os.walk(file_from):
            for file_name in files :
                local_path = os.path.join(root,file_name)
                relative_path = os.path.relpath(local_path,file_from)
                dropbox_path = os.path.join(file_to,relative_path)
                with open(local_path,"rb") as f:
                    dbx.files_upload(f.read(),dropbox_path,mode= WriteMode("overwrite"))

def main():
    access_token = "2QIJd6ghUJwAAAAAAAAAAUKdADUKmuUgLnGbDpaybvDQmktWVYlpE9ZF6QwGzBfL"
    transeferData = TranseferData(access_token)
    file_from= "test.txt"
    file_to = "/test_dropbox/test.txt"
    transeferData.upload_files(file_from,file_to)
    print("file has been moved")

main()

