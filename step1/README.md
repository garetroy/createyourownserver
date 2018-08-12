#The first steps (Backend)

### Setup
    *Just have python and flask installed

### Directory Format 
    You can just copy everything that is in this step.
    The format should be 
    ```
    /
    |
    |--static/ (This is where we will be putting images, javascript, css and others.
             |
             |---javascript/
             |
             |---css/
             |
             |---images/
    |
    |--templates/ (This is where all html will go)
                |
                |---home.html
    |
    |--app.py (The actual server)
    ```

    You can more or less just copy this part of the repository to start your own.

    We will be adding to this later, but for now, this is all you need!

### app.py

    To add your own routes (website.com/[ROUTE]) all you have to do is the following.

    ```python3 
        import flask, os
        from flask import render_template, Flask

        app = flask.Flask(__name___)

        @app.route('/') #at the base route (website.com/)
        def home():
            return flask.render_template('home.html')

        if __name__ == '__main__':
            port = int(os.environ.get('PORT', 5000)
            app.run(debug=True, host='0.0.0.0', port=port)
    ```

    This will get you going the 'root' directory of the website.
    Going to website.com will go to this function, and display home.html

    home.html must be present in templates.

    Notice that you are running this server in debug mode and some host and chosent port.
    You may have to alter this to get it to run on your own machine.

    Inorder to see what you have so far, simply run python3 app.py and navigate
    to 0.0.0.0:5000 in your web browser (may be different if you changed the ip)

   
