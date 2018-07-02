import {NgModule} from '@angular/core';
import {RouterModule, Routes} from '@angular/router';
import { BTCComponent } from './btc/btc.component';
import { ETHComponent } from './eth/eth.component';
import { XRPComponent } from './xrp/xrp.component';

const routes: Routes = [
  {path: '', component: XRPComponent},
  {path: 'eth', component: ETHComponent},
  {path: 'btc', component: BTCComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRouters {}