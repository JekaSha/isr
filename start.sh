#!/bin/bash
cd frontend
npm install
npm run build
cd ..
docker-compose build
docker-compose up
