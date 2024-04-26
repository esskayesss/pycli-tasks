<h3 align="center">pycli-tasks</h3>

This is a simple CLI Task/Todolist manager written in Python. I made this to primarily familiarize myself with 
the Typer and Rich Python libraries. 

### Getting Started
To get a local copy up and running follow these simple steps.
1. Make sure you have Python and Poetry installed and added to PATH
2. Clone the repository
```sh
git clone https://github.com/esskayesss/pycli-tasks.git
```
3. Get the project dependencies
```sh
poetry install
```
4. Run the program as a module
```sh
poetry run python -m src.main
```


### Deliverables
- [x] Tasks Creation
- [x] Tasks Deletion
- [x] Marking Tasks as Done
- [x] Listing Tasks
- [x] Categorizing Tasks
- [x] Prioritizing Tasks
- [ ] Filtering Tasks
- [ ] Searching Tasks
- [ ] Adding Application State to Optimize DB Calls
- [x] Adding and Deleting Categories
- [ ] Adding Fuzzy Finder Menus for Operations [ I miss GoLang so damn much :( ] 
- [ ] Supporting a full-blown TUI
- [ ] Remove the default interactive mode for the CLI
- [ ] Bringing it to the web