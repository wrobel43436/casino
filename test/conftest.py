from flask import Flask
from pytest import fixture

from run import appl


@fixture(scope = 'package')
def app():
    yield appl





@fixture(scope = 'package')
def client(app):
    yield app.test_client()
