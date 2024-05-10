from dependencies.custom_git import clone
from dependencies.custom_dotnet import release
from dependencies.custom_ftp import deploy

cloned = clone('https://github.com/dev372k/Free-API-Store', "main", 'Free-API-Store')
if(cloned):
    released = release("Free-API-Store/Presentation", "Presentation.csproj", "release/net8.0")
    if(released):
            print("Deploying it on server...")   
            deployed = deploy()
            if(deployed):
                print("Deployment successful.")  

            



            