# -*- coding: utf-8 -*-
from Flask-Atomist-Test.swagger import spec
from Flask-Atomist-Test import __version__


def test_document_meta():
    api = spec.to_dict()
    assert api['info']['title'] == 'Flask-Atomist-Test'
    assert api['info']['version'] == __version__
    assert api['info']['description'] == 'Testing out Atomist'


def test_document_health_endpoint():
    api = spec.to_dict()
    assert '/health' in api['paths']
    assert 'get' in api['paths']['/health']
    assert '200' in api['paths']['/health']['get']['responses']
    assert 'string' in api['paths']['/health']['get']['responses']['200']['schema']
    assert '503' in api['paths']['/health']['get']['responses']
    assert 'string' in api['paths']['/health']['get']['responses']['503']['schema']


def test_document_status_endpoint():
    api = spec.to_dict()
    assert '/status' in api['paths']
    assert 'get' in api['paths']['/status']
    assert '200' in api['paths']['/status']['get']['responses']
    assert 'string' in api['paths']['/status']['get']['responses']['200']['schema']


def test_document_flasktest_endpoint():
    api = spec.to_dict()
    assert '/' in api['paths']
    assert 'get' in api['paths']['/']
    assert '200' in api['paths']['/']['get']['responses']
    assert 'string' in api['paths']['/']['get']['responses']['200']['schema']