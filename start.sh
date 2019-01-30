cd api
source env/bin/activate
export FLASK_APP=api.py
export FLASK_DEBUG=True
flask run &
cd ../nuxt
npm run dev &


