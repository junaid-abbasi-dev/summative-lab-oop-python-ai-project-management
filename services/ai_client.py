import ollama

class OllamaClient:
    def __init__(self, model="llama3.2"):
        self.model = model

    def summarize_project(self, project, tasks):
        task_lines = []
        for task in tasks:
            task_lines.append(
                f"- {task.title} ({task.status}), assigned to {task.assigned_to}"
            )
        prompt = (
            "Summarize this project in 3 sentences.\n"
            f"Title: {project.title}\n"
            f"Description: {project.description}\n"
            f"Due: {project.due_date}\n"
            "Tasks:\n"
            + "\n".join(task_lines)
        )
        response = ollama.chat(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
        )
        return response["message"]["content"]