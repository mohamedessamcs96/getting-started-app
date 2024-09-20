# Stage 1: Build the application
FROM node:16 AS build

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy package.json and package-lock.json to the container
COPY package*.json ./

# Install dependencies using npm ci (recommended for CI environments)
RUN npm ci

# Copy the rest of the application code to the container
COPY . .

# Optionally, build your application here (if required, e.g., for frontend build)
# RUN npm run build

# Stage 2: Run the application
FROM node:16

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy only the necessary files from the build stage
COPY --from=build /usr/src/app .

# Expose the port that the app listens on
EXPOSE 3000

# Run the application
CMD ["npm", "start"]
