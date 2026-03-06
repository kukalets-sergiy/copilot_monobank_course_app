FROM node:20-alpine

# Set the working directory
WORKDIR /app

# Copy package.json and package-lock.json (if it exists)
COPY package.json ./
COPY package-lock.json* ./

# Expose port 5173
EXPOSE 5173

# Run the application
CMD [ "npm", "run", "dev", "--", "--host=0.0.0.0", "--port=5173" ]