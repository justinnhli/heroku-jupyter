import traceback
try:
    import os
    import IPython.lib

    c = get_config()

    ### Password protection ###
    # http://jupyter-notebook.readthedocs.io/en/latest/security.html
    passwd = os.environ['JUPYTER_NOTEBOOK_PASSWORD']
    if passwd:
        c.NotebookApp.password = IPython.lib.passwd(passwd)
    else:
        c.NotebookApp.token = ''
        c.NotebookApp.password = ''

except Exception:
    traceback.print_exc()
    # if an exception occurs, notebook normally would get started
    # without password set. For security reasons, execution is stopped.
    exit(-1)
