import json


def saveProject(projectData, fileName):
    with open(fileName, 'w') as json_file:
        json.dump(projectData, json_file)

def loadProject(fileName):
    with open(fileName) as f_in:
        return json.load(f_in)


if __name__ == "__main__":
    my_project = {
        'name': 'John Doe',
        'age': 29
    }
    my_filename = "test_project.json"
    saveProject(my_project, my_filename)
    print("saved")
    my_saved_project = loadProject(my_filename)
    print(my_saved_project)