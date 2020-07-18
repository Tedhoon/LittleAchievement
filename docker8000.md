FROM python:3.6

RUN apt-get update \ 
	&& apt-get install -y --no-install-recommends \
		postgresql-client \
	&& rm -rf /var/lib/apt/lists/*

COPY . /app
# 나의 Django 코드를 컨테이너에 복사합니다.

WORKDIR /app/LittleAchievement/
# 요놈은 CMD 관련이네!

# RUN pip install -r /app/LittleAchievement/requirements.txt  
RUN pip install django
# requirements.txt에 적혀있는 pip 패키지들을 설치합니다.
# requirements.txt경로 /home/ubuntu/LittleAchievement/config/requirements.txt

# RUN chmod 755 /app/start  
# start 파일을 실행 가능하게 합니다.
# chmod 755 /home/ubuntu/LittleAchievement/start  

# /home/ubuntu/-
# 워킹디렉토리를 /app으로 합니다.

EXPOSE 8000  
# 8000번 포트를 expose합니다.

# ENTRYPOINT ["/app/start"]  
# /app/start 파일을 실행시킵니다.
# start => 
    # python manage.py makemigrations
    # python manage.py migrate
    # python manage.py runserver 0.0.0.0:8000



# COPY requirements.txt ./
# RUN pip install -r requirements.txt
# COPY . .
# WORKDIR /app/LittleAchievement

CMD ["python", "manage.py", "makemigrations"]

CMD ["python", "manage.py", "migrate"]

# CMD ["python", "manage.py", "collectstatic"]

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
