from fastapi import FastAPI
from typing import List

app = FastAPI()
Task = []

@app.post("/work/add")
def add_book(task_name, desc):
    Task.append({"task_name": task_name, "desc": desc})
    return Task

@app.put("/work/update")
def update_book(task_name, updated_desc):
    for work in Task:
        if work["task_name"] == task_name:
            work["desc"] = updated_desc
            return Task
    return {"message": "No work found"}

@app.delete("/work/delete")
def delete_book(task_name):
    for work in Task:
        if work["task_name"] == task_name:
            Task.remove(work)
            return Task
    return {"message": "No work found"}

@app.get("/work/get")
def get_all_tasks():
    return Task
