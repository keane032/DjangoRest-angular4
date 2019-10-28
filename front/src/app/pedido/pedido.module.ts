import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { PedidoFormComponent } from './pedido-form/pedido-form.component';
import { FormsModule } from '@angular/forms'
import { RouterModule } from '@angular/router';

@NgModule({
  declarations: [PedidoFormComponent],
  imports: [
    CommonModule,
    FormsModule,
    RouterModule
  ],
  exports: [
    PedidoFormComponent,
  ]
})
export class PedidoModule { }
