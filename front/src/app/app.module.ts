import { Routes, RouterModule } from '@angular/router';

import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import {FormsModule} from '@angular/forms'
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import {ClienteModule} from './user/cliente.module';
import { HttpClientModule } from '@angular/common/http';
import { UserFormComponent } from './user/user-form/user-form.component';
import { PedidoFormComponent } from './pedido/pedido-form/pedido-form.component';
import { PedidoModule } from './pedido/pedido.module';

const rotas: Routes = [
  {path:'user/novo',component:UserFormComponent},
  {path:"pedido/novo", component:PedidoFormComponent}
]

@NgModule({
  declarations: [
    AppComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    ClienteModule,
    FormsModule,
    HttpClientModule,
    PedidoModule,
    RouterModule,
    RouterModule.forRoot(rotas)
  ],
  providers: [],
  bootstrap: [AppComponent]
})


export class AppModule { }
