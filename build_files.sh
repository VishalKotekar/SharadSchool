echo " BUILD START"
pip install -r requirements.txt
python3.8 manage.py collectstatic
echo " BUILD END"
