from flask import redirect
from . import create_app

app = create_app()

@app.route('/')
def redirect_to_api():
    return redirect('/api/v1/calendar/', code=302)

if __name__ == '__main__':
    app.run(debug=True)
