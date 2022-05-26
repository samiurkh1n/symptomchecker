# Symptom Checker

## Setup

First, setup your container. This was developed with [this](https://github.com/microsoft/vscode-dev-containers/blob/main/containers/python-3/README.md) at
python 3.8, for instance.

A .devcontainer is provided if you want to use it.

Then, setup your environment
```console
$ python3 -m venv .venv --prompt="symptomchecker"
$ .venv/bin/activate
(symptomchecker) $ python3 -m pip install -r requirements.txt
```

## Testing

```console
(symptomchecker) $ python3 manage.py test
```

## Deployment

TODO(samiurkh1n): Deploy to Heroku
