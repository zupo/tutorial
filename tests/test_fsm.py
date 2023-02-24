from tutorial import models


def test_fsm(app_request, dbsession):
    model = models.MyModel(name='one', value=55)
    dbsession.add(model)
    dbsession.flush()

    assert model.state == model.states.new

    model.start.set()
    assert model.state == model.states.in_progress

    model.finish.set()
    assert model.state == model.states.done

    model.reset.set()
    assert model.state == model.states.new


def test_fsm_functional(testapp, dbsession):
    model = models.MyModel(name='one', value=55)
    dbsession.add(model)
    dbsession.flush()

    assert model.state == model.states.new

    res = testapp.get('/', status=200)
    assert model.state == model.states.in_progress
    assert model.value == 1

    res = testapp.get('/', status=200)
    assert model.state == model.states.done
    assert model.value == 2

    res = testapp.get('/', status=200)
    assert model.state == model.states.new
    assert model.value == 3
