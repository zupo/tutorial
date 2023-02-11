from tutorial import models
from sqlalchemy_continuum import changeset, version_class, transaction_class
from pyramid.testing import DummyRequest

import transaction
import webtest


def test_history(app):
    TransactionModel = transaction_class(models.MyModel)
    tm = transaction.TransactionManager(explicit=True)

    request = DummyRequest()
    request.client_addr = "1.2.3.4"

    session_factory = app.registry["dbsession_factory"]
    dbsession = models.get_tm_session(session_factory, tm, request)

    # populate DB with one model
    with tm:
        model = models.MyModel(name="one", value=1)
        dbsession.add(model)

        user = models.User(name="foo")
        dbsession.add(user)

    # update the model (in a separate transaction created by webtest)
    testapp = webtest.TestApp(
        app,
        extra_environ={
            "tm.manager": tm,
            "app.dbsession": dbsession,
        },
    )

    testapp.get("/", status=200)

    # assert model was updated and history record created
    with tm:
        one = dbsession.query(models.MyModel).filter(models.MyModel.name == "one").one()
        assert one.value == 2

        assert version_class(models.MyModel).__name__ == "MyModelVersion"
        assert one.versions[0].value == 1
        assert one.versions[1].value == 2

        transactions = dbsession.query(TransactionModel).all()

        # the "populate DB with one model" step above
        assert transactions[0].user == None

        # the "update the model" step above
        user = dbsession.query(models.User).filter(models.User.name == "foo").one()
        assert transactions[1].user == user

    # we committed transactions in this test so we need to clean up
    with tm:
        one = dbsession.query(models.MyModel).filter(models.MyModel.name == "one").one()
        dbsession.delete(one)
