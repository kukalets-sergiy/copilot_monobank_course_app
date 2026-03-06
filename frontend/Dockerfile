FROM node:20-alpine

COPY package.json package-lock.json* ./

EXPOSE 5173

CMD ["vite", "dev", "--host", "0.0.0.0", "--port", "5173"]