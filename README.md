# Examination2-DA115B
Group assignment in the course "Sustainable Development" at Kristianstad University.

This project is an object-oriented Python application of a dice game called 'Pig'. When playing the game versus the computer, the computer's "intelligence" has been divided into 2 separate difficulty levels. These difficulty levels are 'easy' and 'hard', where the easy difficulty level is pretty much a guaranteed win for the player no matter how the player chooses to play. The hard difficulty level utilizes a well-known approach to the game which makes it harder for the player to win every time with this option selected.

## Regenerating Documentation

To regenerate the documentation for this project, then follow this steps:

### Prequisites

Before you start, check that you have the necessary tools installed:

1. [Python](https://python.org/downloads/): Make sure Python is installed on the system.
2. [Sphinx](https://www.sphinx-doc.org/): Sphinx is a documentation generation tool for python. Install by using the following command on the terminal:

----
pip install sphinx
----

### Generating Documentation

1. Navigate to the 'docs' directory in the terminal by:

----
cd path/to/your/project/docs
----

2. Run the following command to generate the HTML documentation:

----
.\make.bat html
----

If you are using macOS or Linux then use:

----
make html
----

This command will then build the documentation and place the html files in the '_build/html' directory.

### Viewing the documentation

1. After generating the documentation, then open the '_build/html' directory
2. Find the 'index.html' file and open it in your web browser.

You can also use a local server to view the documentation by the following command from the '_build/html' directory:

----
python -m http.server
----
