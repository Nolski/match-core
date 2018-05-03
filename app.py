from apistar import App, Route, http
from commcare import CommCareApi

def welcome(name=None):
    if name is None:
        return {'message': 'Welcome to API Star!'}
    return {'message': 'Welcome to API Star, %s!' % name}

def list_forms() -> dict:
    api = CommCareApi()
    return api.list_forms()

def list_cases() -> dict:
    api = CommCareApi()
    return api.list_cases()

def forward_case(request: http.Request) -> dict:
    print(request.body)
    return {}

routes = [
    Route('/', method='GET', handler=welcome),
    Route('/forms', method='GET', handler=list_forms),
    Route('/cases', method='GET', handler=list_cases),
    Route('/forward', method='POST', handler=forward_case),
]

app = App(routes=routes)


if __name__ == '__main__':
    app.serve('127.0.0.1', 5000, debug=True)
