
#frontend

FROM node:14 AS frontend-builder

WORKDIR /frontend

COPY frontend/package*.json ./

RUN npm install

COPY frontend/ .

RUN npm run build


#backend
FROM python:3.9-slim

RUN apt-get update && apt-get install -y build-essential

WORKDIR /app

COPY backend/requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY --from=frontend-builder /frontend/dist /usr/share/nginx/html

COPY backend/ /app/

RUN python manage.py migrate
RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "taskmanager.wsgi:application"]


