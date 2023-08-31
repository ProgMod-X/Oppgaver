import os

def find_readme_and_py_files(root_path):
    a = 0
    for foldername, subfolders, filenames in os.walk(root_path):
        for filename in filenames:
            if filename == "README.md":
                readme_path = os.path.join(foldername, filename)
                py_filename = filename.replace("README.md", "")
                py_files = [f for f in filenames if f.startswith(py_filename) and f.endswith(".py")]
                for py_file in py_files:
                    py_file_path = os.path.join(foldername, py_file)
                    print(f"{readme_path}")
                    print(f"{py_file_path}")
                    a += 1
                    print(a)
                    print()
                    
                    

def main():
    project_root = "/home/ctf/Oppgaver/Grunnleggende-Programmering/" 
    find_readme_and_py_files(project_root)


if __name__ == "__main__":
    main()
