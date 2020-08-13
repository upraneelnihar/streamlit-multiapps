# streamlit-multiapps
A simple framework in python to create multi page web application using streamlit.

# How to Run

1. Clone the repository:
```
$ git clone git@github.com:upraneelnihar/streamlit-multiapps
$ cd streamlit-multiapps
```

2. Install dependencies:
```
$ pip install -r requirements.txt
```

3. Start the application:
```
streamlit run app.py
```

# How to add new app

1. Add a new python file in `apps/`  folder with a function named `app`.

```
# apps/new_app.py

import streamlit as st

def app():
    st.title('New App')
```

2. Now add it to `app.py`

```
from apps import newapp # import your app modules here

app = MultiApp()

# Add all your application here
app.add_app("New App", newapp.app)
```

That's it your new app is added to your application and is live in default browser.