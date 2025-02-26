FROM public.ecr.aws/docker/library/node:20.18.1-bullseye-slim@sha256:deb2485642775da7e9c325b3d91d314d11f294859ac5c6924f0c30b98a1dcbce

WORKDIR /app

COPY package*.json ./
# Enable this line if patch-package is used
# COPY patches ./patches

RUN npm ci

COPY . .

EXPOSE 3000

# nosemgrep: dockerfile.security.missing-user.missing-user
CMD ["npm", "run", "dev", "--", "--host", "--no-open"]
