# serverless-project-example

Example code for the blog post at [https://w11i.me/how-to-structure-a-python-serverless-project](https://w11i.me/how-to-structure-a-python-serverless-project).

## Installing development dependencies

```
python -m pip install -U -r requirements-dev.txt
```

## Running tests

```
make test
```

## Running mypy

```
make mypy
```

## Deploying code

Deploying code requires a configured AWS account and a local installation of [AWS SAM CLI](https://aws.amazon.com/serverless/sam/).

First build the project:

```
sam build
```

Then deploy it:

```
sam deploy --guided
```

The `--guided` flag is only required on the first deployment (or whevever you want to change deployment configuration).
