FROM node:22-alpine
WORKDIR /app
COPY frontend/package.json /app/
COPY frontend/src /app/src
RUN npm install
CMD ["npm", "run", "dev"]
