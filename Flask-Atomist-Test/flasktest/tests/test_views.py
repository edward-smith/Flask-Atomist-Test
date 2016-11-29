# -*- coding: utf-8 -*-
from flask import url_for


def test_flasktest_index(client):
    res = client.get(url_for('flasktest_app.index'))
    assert res.data == b'Hello World!'
