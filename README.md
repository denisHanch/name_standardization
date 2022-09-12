# Normalization task
Script fot hte normalization of the compound names

To run locally:
1) Create new python environment (e.g. using `pyenv`)
2) Install requirements: `pip install -r requirements.txt`
3) Run: `python ./src/main.py`
4) When script finished its run, check file `list_of_normalized_names.csv`

To run in docker:
1) Build docker container: `docker build -t IMAGE_NAME .`
2) Run docker container: `docker run -d --name CONTAINER_NAME IMAGE_NAME`
3) Check the table of normalized names: `docker logs CONTAINER_NAME`