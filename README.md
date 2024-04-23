# Examination2-DA115B
Group assignment in the course "Sustainable Development" at Kristianstad University.

This project is an object-oriented Python application of a dice game called 'Pig'. When playing the game versus the computer, the computer's "intelligence" has been divided into 2 separate difficulty levels. These difficulty levels are 'easy' and 'hard', where the easy difficulty level is pretty much a guaranteed win for the player no matter how the player chooses to play. The hard difficulty level utilizes a well-known approach to the game which makes it harder for the player to win every time with this option selected.

## Installation of game

To run this project locally, follow these steps:

1. Clone the repository to your local computer
2. Go to the projects directory
3. Install the required dependencies using:

**pip install -r requirements.txt**

## Usage

1. Navigate to the project directory in the terminal with:

**cd path/to/the/project/**

2. Run the game:

**python main.py**






## Regenerating Documentation

To regenerate the documentation for this project, then follow this steps:

### Prequisites

Before you start, check that you have the necessary tools installed:

1. [Python](https://python.org/downloads/): Make sure Python is installed on the system.
2. [Sphinx](https://www.sphinx-doc.org/): Sphinx is a documentation generation tool for python. Install by using the following command on the terminal:

**pip install sphinx**

### Generating Documentation

1. Navigate to the 'docs' directory in the terminal by:

**cd path/to/your/project/docs**

2. Run the following command to generate the HTML documentation:

**.\make.bat html**

If you are using macOS or Linux then use:

**make html**

This command will then build the documentation and place the html files in the '_build/html' directory.

### Viewing the documentation

1. After generating the documentation, then open the '_build/html' directory
2. Find the 'index.html' file and open it in your web browser.

You can also use a local server to view the documentation by the following command from the '_build/html' directory:

**python -m http.server**







## Running the Complete Test Suite and Generating Coverage Report

To run the complete test suite and generate a coverage report for this project, then follow the instructions below:

### Prerequisites

Before you start, ensure that you have the necessary tools installed:

1. Python: Check that python is installed on your system
2. Pytest: 'pytest' is a testing framework for python. Install it by using this command:

**pip install pytest**


3. Coverage: 'coverage' is also a tool for measuring code coverage of python programs. Install it by using this command:

**pip install coverage**

### Running Tests

1. Open a terminal and find the root directory of the project with command:

**cd path/to/your/project**

2. Run the complete test suite using the following command:

**python -m coverage run -m unittest discover <your directory here>**

### Generating coverage report

1. Then after running all the tests, generate a coverage report by the following command and to see the report:

**python -m coverage report**

This will display a summary of the code coverage. To create a html report type the following command:

**python -m coverage html**


You can open the generated html report located in the 'htmlcov' directory.

Now with following the instructions you have run the complete test suite and generated a coverage report for the project.





## Generating UML Diagrams

To be able to generate UML diagrams for the python code in the project, you can use the pyreverse tool with the Graphviz. Here are the following steps:

### Prerequisites

Before you start, ensure that you have the necessary tools installed:

1. Python: Make sure python is installed on the system.
2. Graphviz: Install Graphviz from the offical website (https://www.graphviz.org/download/#windows) and follow the installation instructions there.

If you are using Linux you can instead use on the terminal: sudo apt-get install graphviz

If you are using macOS you can instead use on the terminal: sudo port install graphviz


### Generating UML Diagrams

1. Open the terminal and find the path to the directory which contains your python files:

**cd path/to/your/project/**


2. Run the following command to generate UML diagrams in PNG format:

**pyreverse -o png -p directory-name file1.py file2.py file3.py .... file7.py**

Now Graphviz will generate PNG files with UML diagrams for each module.

You will find the generated PNG files in the same directory as the python files.

