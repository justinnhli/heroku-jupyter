# heroku-jupyter

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

Based on [pl31/heroku-jupyter](https://github.com/pl31/heroku-jupyter). Differences:

* Removed dependence on [conda](https://conda.io/docs/intro.html), which greatly reduces the compiled slug size. The space allows the addition of packages such as [pandas](http://pandas.pydata.org/), [scikit-learn](http://scikit-learn.org/stable/), [matplotlib](http://matplotlib.org/), and [bokeh](http://bokeh.pydata.org/en/latest/) while still coming in under 200MB.
* Removed [`pgcontents`](https://github.com/quantopian/pgcontents), to take advantage of the latest Jupyter and IPython releases (see [this bug](https://github.com/quantopian/pgcontents/issues/28) in `pgcontents`). **This means notebooks will not be saved.** Download your notebooks to ensure persistence across sessions.
* Removed CloudFoundry components and Jupyter Notebook extensions, mostly so I don't have to maintain code that I don't use. Fork this repository and add them back in as desired.
* Defaults to no password protection if `JUPYTER_NOTEBOOK_PASSWORD` is not set.
