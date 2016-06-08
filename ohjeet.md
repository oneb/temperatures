Nämä ohjeet ovat Ubuntu 14.04:lle.

Asenna tarvittavat:

    sudo apt-get update
    sudo apt-get install python-pip python-dev python-virtualenv   

Kloonaa repositorio:

    git clone http://github.com/oneb/temperatures

Luo virtualenv ja asenna requirementsit:

    virtualenv -p python3 temperatures-env
    source temperatures-env/bin/activate
    pip install -r temperatures/requirements.txt

Hanki haltuusi tiedosto settings_secret.py, jossa on määritelty SECRET_KEY. Kopioi settings_secret.py alikansioon temperatures/ (jossa on myös settings_common.py)

Sitten tee nämä:

    ./manage.py makemigrations
    ./manage.py migrate

Käynnistä serveri:

    gunicorn -b 0.0.0.0:8000 temperatures.wsgi:application

Mene selaimella osoitteeseen http:/127.0.0.1:8000 nähdäksesi listan lämpötilalukemista. (Tai 127.0.0.1:n sijaan nykyisen hostin IP).

Generoi 1000 testilukemaa:

    ./manage.py populate 1000 

Poista kaikki lukemat:

    ./manage.py del_temperatures

Luo curlilla uusi lukema:

    curl -i -H 'Content-Type: application/json' -d '{"tmp":99.99}' http://127.0.0.1:8000/api/readings/

Katso curlilla API:n antamaa listaa lukemista:

    curl -X GET 127.0.0.1:8000/api/readings/ 
