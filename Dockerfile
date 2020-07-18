FROM ubuntu:18.04

# code copying
COPY . /app
WORKDIR /app/LittleAchievement/

# ubuntu 기본 세팅으으으으
RUN sudo apt-get update
RUN sudo apt-get install build-essential
RUN sudo apt-get install python3
RUN sudo apt-get install python3-pip
RUN sudo pip3 install --upgrade pip

# 가상환경 만들고 킵시당
RUN sudo apt-get install virtualenv
RUN virtualenv -p python3 venv
RUN source /app/LittleAchievement/venv/bin/activate

# pip package 깔자!!!
RUN pip install -r /app/LittleAchievement/requirements.txt  

# uwsgi install
RUN pip install uwsgi 

# 이줴 nginx
RUN sudo apt-get install nginx



# expose port 
EXPOSE 80 
EXPOSE 8000
EXPOSE 8080 


CMD python manage.py collectstatic
CMD python manage.py makemigrations
CMD python manage.py migrate

RUN uwsgi --ini /app/LittleAchievement/uwsgi.ini 
# 근데 얘는 run인감?

# nginx 설정해주고
RUN sudo service nginx reload





WORKDIR /app/LittleAchievement/

RUN pip install -r /app/LittleAchievement/requirements.txt  