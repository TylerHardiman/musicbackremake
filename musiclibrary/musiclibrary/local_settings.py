SECRET_KEY = 'django-insecure-_3@w5&m_u$%fv5g@d)_=@8!nd#65($1*c#q9tf3mve#b)lc*(g'
DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'music_library_database',
        'USER': 'root',
        'PASSWORD': 'BingBong',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'autocommit': 'True',
        }
        
        
    }
}