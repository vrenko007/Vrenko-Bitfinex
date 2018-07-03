import { Injectable } from '@angular/core';
import { Socket } from 'ngx-socket-io';
import { Observable } from 'rxjs/Observable'
import 'rxjs/add/operator/share'; 


@Injectable()
export class DataService {

  constructor(private socket: Socket) { }

    sendMessage(action: string, msg: string){
        this.socket.emit(action, {"room":msg});
    }

    getMessage() {
        return this.socket
            .fromEvent("transaction")
    }
}