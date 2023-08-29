import openai
import os
from nbformat import v4 as nb

# OpenAI API Key
openai.api_key = "YOUR_OPENAI_API_KEY"

def generate_solution(prompt):
    response = openai.Completion.create(
        engine="davinci-codex",
        prompt=prompt,
        max_tokens=1500,
        temperature=0.7
    )
    return response.choices[0].text.strip()

def process_files(oppgave_path, solve_path):
    with open(oppgave_path, "r") as oppgave_file:
        oppgave_text = oppgave_file.read()

    with open(solve_path, "r") as solve_file:
        solve_code = solve_file.read()

    prompt = f"# Oppgave\n\n{oppgave_text}\n\n# Løsningsforslag\n\n```python\n{solve_code}\n```"
    solution = generate_solution(prompt)

    notebook = nb.new_notebook()
    notebook.cells.append(nb.new_markdown_cell(prompt))
    notebook.cells.append(nb.new_markdown_cell(solution))

    notebook_path = oppgave_path.replace("oppgave.md", "solution.ipynb")
    with open(notebook_path, "w") as notebook_file:
        nb.write(notebook, notebook_file)

def main():
    oppgave_path = os.path.abspath(sys.argv[1])
    solve_path = oppgave_path.replace("oppgave.md", "solve.py")
    process_files(oppgave_path, solve_path)

if __name__ == "__main__":
    main()
