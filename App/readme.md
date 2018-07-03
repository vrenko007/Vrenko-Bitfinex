# Readme

## MySql

 1. install mysql
 2. create database `Vrenko-Bitfinex`
 3. create user: `Vrenko-Bitfinex` with password: `Super111Complicated222`

## Python

 1. install python 3.6.5
 2. install pip + pipenv
 3. move to backend/
 4. run `pipenv install`
 5. make bootstrap.sh runnable with `chmod +x ./bootstrap.sh`
 6. run `./bootstrap.sh`
 7. leave running

## Angular
 1. install node, npm, angular-cli
 2. move to Client/
 3. run `npm install`
 4. run `ng serve`

App should be running on <http://127.0.0.1:4200> or port stated in command line

If python app isn't served on port 5000 you need to update port in SocketIO config in `Client/app/app.module.ts`
