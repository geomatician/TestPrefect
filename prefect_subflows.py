from prefect import flow, task

@task(name="Print Hello")
def print_hello(name):
    msg = f"Hello {name}!"
    print(msg)
    return msg

@flow(name="Subflow1")
def my_subflow_one(msg):
    print(f"Subflow 1 says: {msg}")

@flow(name="Subflow2")
def my_subflow_two(msg):
    print(f"Subflow 2 says: {msg}")

@flow(name='hello_world',log_prints=True)
def hello_world(name="world"):
    message = print_hello(name)
    my_subflow_one(message)
    my_subflow_two(message)

if __name__ == "main":
    hello_world('earth')