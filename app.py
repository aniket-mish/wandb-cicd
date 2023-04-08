import wandb

print(f"The wandb version is {wandb.__version__}")

# pytest
assert (wandb.__version__ == '2.12.3', f"Expected version is {wandb.__version__} and we got '2.12.3'")
