from urllib import request
from project import Project

import toml

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        my_toml = toml.loads(request.urlopen(self._url).read().decode("utf-8"))
        
        name = my_toml["tool"]["poetry"]["name"]
        description = my_toml["tool"]["poetry"]["description"]
        
        dep = list(my_toml["tool"]["poetry"]["dependencies"])
        dev_dep = list(my_toml["tool"]["poetry"]["dev-dependencies"])
        
        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(name, description, dep, dev_dep)
