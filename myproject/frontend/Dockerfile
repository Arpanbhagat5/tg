# Dockerfile for React app (assuming it's a Node.js app)
FROM node:16

# Set working directory
WORKDIR /app

# Install dependencies
COPY package.json package-lock.json ./
RUN npm install

# Copy the rest of the frontend code
COPY . .

# Expose the port the app runs on
EXPOSE 3000

# Start the frontend
CMD ["npm", "start"]