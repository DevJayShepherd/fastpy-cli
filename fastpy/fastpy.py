from datetime import datetime
from typer import Typer

app = Typer()


@app.command()
def hello_fastpy():
    print("You found me!")


@app.command()
def get_date():
    print(datetime.now().date())


if __name__ == "__main__":
    app()

