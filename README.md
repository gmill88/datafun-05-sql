# datafun-05-sql

## Project start
1. Start a new repository and select default README.md
2. Clone the repository to local environment. Used VS Code functionality to clone the repository. 
3. Open the project and activate the virtual environment
```bash
python3 -m venv .venv
source .venv/bin/activate
```
4. Install dependencies pyarrow and pandas into the .venv
```bash
python3 -m pip install pandas pyarrow
```
5. Freeze dependencies into requirements.txt
 ```bash
 python3 -m pip freeze > requirements.txt
  ```
  6. Git add and commit then push to GitHub
```bash
git add .
git commit -m "initial comment"
git push origin main   
``` 
7. Use touch to create project file