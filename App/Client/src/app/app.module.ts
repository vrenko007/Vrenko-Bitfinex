import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppComponent } from './app.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { FlexLayoutModule } from '@angular/flex-layout';
import { MaterialModule } from './material.module';
import { BTCComponent } from './btc/btc.component';
import { ETHComponent } from './eth/eth.component';
import { XRPComponent } from './xrp/xrp.component';
import { DataService } from './data/data.service';
import { AppRouters } from './app.routes';
import { jqxChartComponent } from '../../node_modules/jqwidgets-scripts/jqwidgets-ts/angular_jqxchart';
import { SocketIoModule, SocketIoConfig } from 'ngx-socket-io';

const config: SocketIoConfig = { url: 'http://vrenko-bitfinex.westeurope.cloudapp.azure.com:5000', options: {} };

@NgModule({
  declarations: [
    AppComponent,
    BTCComponent,
    ETHComponent,
    XRPComponent,
    jqxChartComponent
  ],
  imports: [
    BrowserModule,
    BrowserAnimationsModule,
    MaterialModule,
    FlexLayoutModule,
    AppRouters,
    SocketIoModule.forRoot(config) 
  ],
  providers: [DataService],
  bootstrap: [AppComponent]
})
export class AppModule { }
