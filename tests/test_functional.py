from tutorial import models

def test_my_view_success(testapp, dbsession, dummy_request):
    dbsession.info["request"] = dummy_request

    model = models.MyModel(name='one', value=55)
    dbsession.add(model)
    dbsession.flush()

    res = testapp.get('/', status=200)
    assert res.body

def test_notfound(testapp):
    res = testapp.get('/badurl', status=404)
    assert res.status_code == 404
