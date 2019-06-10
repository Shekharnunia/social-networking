## Running the Project Locally

First, clone the repository to your local machine:

```bash
git clone https://github.com/Shekharnunia/social-networking.git
```

Install the requirements:

```bash
pip install -r requirements.txt
```

Change to source directory:

```bash
cd src
```

Create the database:

```bash
python manage.py migrate
```

Finally, run the development server:

```bash
python manage.py runserver
```

The project will be available at **127.0.0.1:8000**.

