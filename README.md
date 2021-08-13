iris-analysis
==============================

Sample or example repository demonstrating some good workflows when 
working with Git and Jupyter notebooks.

Accompanying presentation available: [Slides](https://docs.google.com/presentation/d/1WZp_V-jQM4dZru19xitD3kiP7K9UaTrdDZ9vQtWSftI/edit?usp=sharing)

A detailed summary of the 'script' I followed when doing 
my code changes is made available in 
[this markdown document](report/DemoScript).



Getting Started Instructions 
==============================

How to start: 

Get Data and Start Docker Container:

```terminal
git clone https://github.com/cybera/fellowship-iris-example.git
cd fellowship-iris-example
docker-compose up --build -d
```

Open web browser at localhost:8200.

Open text editor of your choice. 

Docker Setup
--------------------

### Installation
Before proceeding further, please install [Docker](https://www.docker.com/) following the instructions provided in the [link here](https://docs.docker.com/get-docker/) for your choice of operating system. 

### Setup 

From this project folder run the following command in your terminal to build and deploy the JupyterLab container:
```
docker-compose up --build
```
Use `CTRL + C` to stop JupyterLab and exit the docker container. 

To run the container in detached mode add `-d` as follows:
```
docker-compose up --build -d
```

If you have successfully built and deployed the JupyterLab image container using either of the above commands, you can access the web interface of the JupyterLab at 
```
http://localhost:8200
```

You might be prompted to enter the token while accessing the `http://localhost:8200`. The token can be obtained from the logs of the running JupyterLab container as follows. 

```
docker logs <container-id>
```

To view the list of all the containers and get the container id of the JupyterLab, run 
```
docker ps -a
```


Project Organization
------------
Folder structure or organziation for this project:
```
├── README.md                       <- The top-level README for developers using this project.
├── .gitignore                      <- Ignores files that shouldn't go into git (e.g. ./data/).
│
├── report                          <- The final report, figures, and any reference materials.
│
├── docker-compose.yml              <- Container instructions used when running docker-compose.
├── docker
│   ├── Dockerfile                  <- Dockerfile for building container.
│   └── requirements.txt            <- Specifies additional python packages to install in container.
│
├── data
│   ├── processed                   <- The final, canonical data sets for modeling.
│   └── raw                         <- The original, immutable data dump. (make changes to copies only.)
│
├── models                          <- Trained and serialized models, model predictions, or model summaries.
│
├── notebooks                       <- Jupyter notebooks. Naming convention is a number (for ordering),
│                                      the creator's initials, and a short `-` delimited description.
│
└── scripts                   
     ├── data                       <- Scripts to download or generate data.
     ├── features                   <- Scripts to turn raw data into features for modeling.
     ├── models                     <- Scripts to train models and then use trained models to make.
     └── visualization              <- Scripts to create exploratory and results oriented visualizations.
```


You can regenerate similar on *nix systems using:
     ```$tree -a -I '.git|.gitkeep|__init__.py'```

<p><small>Project layout based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>


