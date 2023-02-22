from prefect import flow, get_run_logger, task
from platform import node, platform

@task
def cowsay(msg):
    print(f"{msg}!")

@task
def print_hello(name):
    print(f"Hello {name}!")

@flow
def check():
    logger = get_run_logger()
    logger.info(f"Network: {node()}. ✅")
    logger.info(f"Instance: {platform()}. ✅")



if __name__ == "__main__":
    check()