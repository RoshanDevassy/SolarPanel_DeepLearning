# Install dependencies only when needed
FROM node:18-alpine AS deps
WORKDIR /app
COPY package.json package-lock.json* ./
RUN npm install

# Build the app
FROM node:18-alpine AS builder
WORKDIR /app

# Accept environment variable for build
ARG NEXT_PUBLIC_API_BASE_URL
ENV NEXT_PUBLIC_API_BASE_URL=$NEXT_PUBLIC_API_BASE_URL

COPY --from=deps /app/node_modules ./node_modules
COPY . .

# Optional: log env for debugging
RUN echo "Building with NEXT_PUBLIC_API_BASE_URL=$NEXT_PUBLIC_API_BASE_URL"

# Build the Next.js app with env variable
RUN npm run build

# Serve the app
FROM node:18-alpine AS runner
WORKDIR /app

# Copy built files
COPY --from=builder /app/public ./public
COPY --from=builder /app/.next ./.next
COPY --from=builder /app/node_modules ./node_modules
COPY --from=builder /app/package.json ./package.json

EXPOSE 3000

CMD ["npm", "start"]
