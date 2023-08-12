FROM node:16.5.0
COPY . /work/
WORKDIR /work
RUN yarn global add @vue/cli
RUN yarn install
EXPOSE 8080
VOLUME /data
CMD ["yarn", "serve"]
