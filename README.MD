# Tutorial - https://www.youtube.com/watch?v=SdTzwYmsgoU

# Install Python 3.x

# Create Git Repo for the project with a README file and clone

 From the repo directory on the machine run code

# Create Python Virtual Environments from vscode therminal 

    https://code.visualstudio.com/docs/setup/mac 

    https://docs.python.org/3/library/venv.html

    https://packaging.python.org/en/latest/guides/

# installing-using-pip-and-virtual-environments/

```bash
    python3 -m venv <Name>
    source activate <Name>/src/bin/activate
    python3 -m pip install flask
```

Should be prompted to source venv by vscode

Add the .gitinore file to include the venv

# Installing Python VS Code Extension

# Sample Flask Application 
https://flask.palletsprojects.com/en/2.2.x/quickstart/#a-minimal-application
    

# Using Pip to Freeze Python Dependencies
```bash
    python3 -m pip freeze > requirements.txt 
    python3 -m pip install -r requirements.txt
```

# Building the docker image using Dockerfile
```bash
    docker build -t webapp:1.0 .
    docker run -d -p 80:5000 --name web webapp:1.0
```

# Writing Docker Compose file
```bash
    docker-compose build
    docker-compose up -d
    docker compose down
```

# Writing Kubernetes Manifest files for the application
```bash
    minikube service --all
```

# Creating Helm Chart
```bash
    helm create webapp
    update the deployment and service information
    helm template webapp
    helm install webapp webapp
    helm list
    helm uninstall webapp
```


