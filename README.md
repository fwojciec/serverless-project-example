# serverless-project-example

Example code for the blog post at [https://w11i.me/how-to-structure-a-python-serverless-project](https://w11i.me/how-to-structure-a-python-serverless-project).

## Developing

To prepare the project for local development it's necessary to install the shared package in editable mode and install the dev dependencies. Run:

```
make develop
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
