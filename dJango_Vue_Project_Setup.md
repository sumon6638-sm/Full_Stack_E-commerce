from audioop import add


Go to File and
virtualenv environment_3_8_2
source environment_3_8_2/bin/activate

pip install virtualenv
pip install django
pip install django-rest-framework --> Create api in the backend
pip install django-cors-headers --> between api and backend will working securely
pip install djoser --> helps us for authentication users and helps create user login get a token for authentication
pip install pillow --> help us resize images, this is a python image library
pip install stripe --> For transection

pip install virtualenv && pip install django && pip install django-rest-framework && pip install django-cors-headers && pip install djoser && pip install pillow && pip install stripe && pip install matplotlib && pip install sqlalchemy

django-admin startproject django_backend
cd django_backend
python manage.py startapp appName
and add this app in setting in django_backend in INSTALLED_APPS


1. Then go to project_dJango --> setting.py -->
  a. add them in INSTALLED_APPS
    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',
    'djoser',
  b. add it in MIDDLEWARE
    'corsheaders.middleware.CorsMiddleware',
  c. add it in bottom
    CORS_ORIGIN_ALLOW_ALL = True

2. Then go to urls.py and add them
  a. from django.urls import path, include
  b. path('api/v1/', include('djoser.urls')),
     path('api/v1/', include('djoser.urls.authtoken')),


python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
Then goto --> http://127.0.0.1:8000/admin

Then goto root folder of environment --> 
1. vue create project_name (Babel, Router, Vuex, CSS Pre-processors, 3, Y, dart-saas, dedicated config files, N) --> create a project
2. cd project_name --> 
    a. yarn add axios && yarn add -D tailwindcss postcss autoprefixer
    b. npx tailwindcss init -p
    c. goto tailwind.config.js and add
        content: [
          "./index.html",
          "./src/**/*.{vue,js,ts,jsx,tsx}",
        ],
    d. create index.css in src and add
        @tailwind base;
        @tailwind components;
        @tailwind utilities;
    e. goto --> src/main.js and add
        import './index.css'
    f. goto --> package.json and add it in rules under eslintConfig
    	"vue/multi-word-component-names": "off"
    g. goto --> vscode settings and add
    	"eslint.workingDirectories": [
		{
		    "mode": "auto"
		}
	    ],
    h. add fontawesome in index.html -->
    	<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.1.1/css/all.min.css" />

3. yarn run dev
