"""MLCube handler file"""
import os
import subprocess

import typer
import yaml

from selection import Predictor

typer_app = typer.Typer()


class DownloadTask:
    """Download samples and eval data"""

    @staticmethod
    def run(parameters_file: str, output_path: str) -> None:

        cmd = "python3 download_data.py"
        cmd += f" --parameters_file={parameters_file} --output_path={output_path}"
        splitted_cmd = cmd.split()

        process = subprocess.Popen(splitted_cmd, cwd=".")
        process.wait()


class SelectTask:
    """Run select algorithm"""

    @staticmethod
    def run(
        input_path: str, embeddings_path: str, parameters_file: str, output_path: str
    ) -> None:

        with open(parameters_file, "r") as f:
            params = yaml.full_load(f)

        print("Creating predictor")
        predictor = Predictor(embeddings_path)
        predictor.closest_and_furthest(
            input_path, output_path, params["n_closest"], params["n_random"]
        )


class EvaluateTask:
    """Execute evaluation script"""

    @staticmethod
    def run(eval_path: str, log_path: str) -> None:

        env = os.environ.copy()
        env.update({"eval_path": eval_path, "log_path": log_path})

        process = subprocess.Popen("./run_evaluate.sh", cwd=".", env=env)
        process.wait()


@typer_app.command("download")
def download(
    parameters_file: str = typer.Option(..., "--parameters_file"),
    output_path: str = typer.Option(..., "--output_path"),
):
    DownloadTask.run(parameters_file, output_path)


@typer_app.command("select")
def select(
    input_path: str = typer.Option(..., "--input_path"),
    embeddings_path: str = typer.Option(..., "--embeddings_path"),
    parameters_file: str = typer.Option(..., "--parameters_file"),
    output_path: str = typer.Option(..., "--output_path"),
):
    SelectTask.run(input_path, embeddings_path, parameters_file, output_path)


@typer_app.command("evaluate")
def evaluate(
    eval_path: str = typer.Option(..., "--eval_path"),
    log_path: str = typer.Option(..., "--log_path"),
):
    EvaluateTask.run(eval_path, log_path)


if __name__ == "__main__":
    typer_app()
