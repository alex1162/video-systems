# Practice 4 - CDN & docker for encoding

This is a brief manual on how we have performed each task of the practice and the steps to follow to prove its functionality.

To do this practice we will use FastAPI. We start by installing fastapi following the steps from its website. We do so by running the command:

*> pip install fastapi*

We then proceed to create a new project folder in our directory called practice1.

Here we will **create** a virtual environment:

*> python -m venv .venv*

And then **activate** it:

*> .venv\Scripts\activate (windows, PowerShell)*

*> source .venv/bin/activate (linux)*

After installing Docker Desktop, we create a dockerfile. We will call it *Dockerfile_api* and it will contain the necessary information to run the api. We store it in a subfolder called *docker*, which will contain related files. 

We later added a requirements.txt file which contains the libraries that need to be installed in order to run the project. This file is stored in the *api* folder, which is described later on.

We create a new dockerfile called Dockerfile_ffmpeg. We get ffmpeg from *jrottenberg/ffmpeg:latest*, which already prepares a minimalist Docker image with FFmpeg. As we will need to run continuously this docker in the background (to be able to call the functions that depend on it), we add a command to do so. We also add the directory of the media folder, which will be shared with the api docker and will be used to store the media we will use. 

To **launch the application**, after activating the virtual environment (*.venv\Scripts\activate*) and opening the docker desktop app (without closing it), we run the following command to build the docker-compose file inside the docker folder: 

*> cd .\docker*
*> docker-compose up --build*

We then can access the application through our browser, using the URL: *localhost:8000*

To stop running the app, we must press Ctrl+C twice (as the ffmpeg docker is running with a command which allows it to not stop, we must force it to do so).
