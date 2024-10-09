# dockerfile 
# (YOUR_NAME) (YOUR_STUDENT_ID)

FROM python:3.12
WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt
COPY . /app/
EXPOSE 8000
CMD ["python", "firstproject/formsDemo/manage.py", "runserver", "0.0.0.0:8000"]