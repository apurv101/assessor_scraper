# assessor_scraper



## AWS
sudo apt update
sudo apt install python3-pip -y
pip3 install selenium flask usaddress
wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo apt-key add -
echo 'deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main' | sudo tee /etc/apt/sources.list.d/google-chrome.list
sudo apt-get update
sudo apt-get install google-chrome-stable -y
sudo apt install firefox -y



mkdir drivers
cd drivers
wget https://github.com/mozilla/geckodriver/releases/download/v0.24.0/geckodriver-v0.24.0-linux64.tar.gz
wget https://chromedriver.storage.googleapis.com/75.0.3770.90/chromedriver_linux64.zip
sudo apt install unzip -y
unzip chromedriver_linux64.zip
tar xvzf geckodriver-v0.24.0-linux64.tar.gz




cd ..

psudo() { sudo env PATH="$PATH" "$@"; } 

scp -i "qwerty.pem" tester.py ubuntu@ec2-54-145-187-235.compute-1.amazonaws.com:tester.py
scp -i "qwerty.pem" app_aws.zip ubuntu@ec2-54-145-187-235.compute-1.amazonaws.com:app_aws.zip

scp -i "autoparts.pem" advance_pro_scraper1.py ubuntu@ec2-54-234-49-121.compute-1.amazonaws.com:advance_pro_scraper1.py

scp -i "autoparts.pem" somefile.csv ubuntu@ec2-54-234-49-121.compute-1.amazonaws.com:somefile.csv

scp -i "autoparts.pem" done_till_here.txt ubuntu@ec2-54-234-49-121.compute-1.amazonaws.com:done_till_here.txt


scp -i "autoparts.pem" advance_pro_scraper1.py ubuntu@ec2-54-234-49-121.compute-1.amazonaws.com:advance_pro_scraper1.py

python3 tester.py

curl 54.145.187.235/alameda -d '{"address_string": "2313 Oregon St, Berkeley, CA"}' -H 'Content-Type: application/json'



curl http://127.0.0.1:5000/alameda -d '{"address_string": "2313 Oregon St, Berkeley, CA"}' -H 'Content-Type: application/json'

curl https://giant-mayfly-84.localtunnel.me/alameda -d '{"address_string": "2313 Oregon St, Berkeley, CA"}' -H 'Content-Type: application/json'

curl http://127.0.0.1:5000/sacramento -d '{"address_string": "4816 Emerson st"}' -H 'Content-Type: application/json'

curl https://giant-mayfly-84.localtunnel.me/sacramento -d '{"address_string": "4816 Emerson st"}' -H 'Content-Type: application/json'

curl http://127.0.0.1:5000/san_francisco -d '{"address_string": "1557 fulton st"}' -H 'Content-Type: application/json'

curl https://giant-mayfly-84.localtunnel.me/san_francisco -d '{"address_string": "1557 fulton st"}' -H 'Content-Type: application/json'

curl http://127.0.0.1:5000/san_mateo -d '{"address_string": "527 miller ave, south san francisco"}' -H 'Content-Type: application/json'

curl https://giant-mayfly-84.localtunnel.me/san_mateo -d '{"address_string": "527 miller ave, south san francisco"}' -H 'Content-Type: application/json'

curl http://127.0.0.1:5000/los_angeles -d '{"address_string": "3836 hayvenhurst ave"}' -H 'Content-Type: application/json'

curl https://giant-mayfly-84.localtunnel.me/los_angeles -d '{"address_string": "3836 hayvenhurst ave"}' -H 'Content-Type: application/json'




## HEROKU

git add .
git commit -m "First Commit"
git remote -v
heroku buildpacks:add heroku/chromedriver
heroku buildpacks:add heroku/python
heroku buildpacks:add heroku/google-chrome
git push heroku master

curl https://sleepy-dawn-51371.herokuapp.com/san_mateo -d '{"address_string": "527 miller ave, south san francisco"}' -H 'Content-Type: application/json'
